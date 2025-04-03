# activate nearest .venv based on the presence of pyproject.toml
activate_nearest_venv() {
    local dir=$PWD

    while [[ "$dir" != "/" ]]; do
        if [[ -f "$dir/pyproject.toml" ]]; then
            if [[ -d "$dir/.venv" ]]; then
                if [[ "$VIRTUAL_ENV" != "$dir/.venv" ]]; then
                    echo "▶️ activating $dir/.venv"
                    source "$dir/.venv/bin/activate"
                fi
                return
            else
                echo -e "\033[31mWarning! local .venv not found. Create it using \`make venv_create\`.\033[0m"
                return
            fi
        fi
        dir="$(dirname "$dir")"
    done

    while [[ -n "$VIRTUAL_ENV" ]]; do
        echo "⏹ deactivating $VIRTUAL_ENV"
        deactivate
    done
}

# override the 'cd' command
cd() {
    builtin cd "$@" && activate_nearest_venv
}

# activate .venv for new shell sessions
activate_nearest_venv
