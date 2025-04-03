[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# provider_builder_{{ cookiecutter.project_name }}

Add a short description here!

## Description

Description for project: provider_builder_{{ cookiecutter.project_name }}.

## Development

A Makefile is provided to automate the most common tasks.

To list all available commands type:

```shell
make help
```

## Version pinning
You are expected to pin the version of the depdency of `data-components` (and also `as-components` if you are using it). A test will fail if the version is not pinned, and it will tell you the correct version to use. To pin the version:
1. modify the Pipfile with the correct version of `data-components`
1. delete the `Pipfile.lock`
1. run `make init`
