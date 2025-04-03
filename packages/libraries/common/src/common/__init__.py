from pathlib import Path
import toml


def get_version():
    pyproject_path = Path(__file__).parent / "../../pyproject.toml"
    with open(pyproject_path, "r") as f:
        pyproject = toml.load(f)
    return pyproject["tool"]["poetry"]["version"]


__version__ = get_version()
