[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# DEMO ETL Monorepo

### Description

This repo dmoes how to strucutre ETLs

### Setup

- Dependencies (use the proper package manager in parenthesis for your environment)

```bash
sudo (apt/brew) install install direnv
sudo (apt/brew) install pipx
sudo (apt/brew) install pyenv  # reads .python-version file in root when creating venvs
sudo (apt/brew) install zoxide # for faster navigation
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
pipx ensurepath
pipx install 'poetry >= 1'
pipx install pre-commit
```

### Operations

- Create New ETL:

```bash
make new-etl
```

- Run pre-commit hooks in the entire project

```bash
make pre-commit
```
