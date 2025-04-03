# provider_prototype

Prototype for the construction of a monolitic repo for a new or existing provider based on [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)

## Setup environment

If you don't have cookiecutter, you can install it with:

```
$ pip3 install cookiecutter
```

Note: if you have an old version of cookiecutter (< 1.7.x) you should reinstall in order to user remote git repositories.

## Creating ETL Job

In order to create an ETL job, run the following command:

```
$ cookiecutter git+ssh://git@host/prototype
```

To create the virtual environment together with environment files:

```
make setup
```
## Managing environment

Everything inside a `./tmp/` directory will be ignored. Use this directory to put your configuration files while testing.

The docker container will pick up a `.env` file with the environment variables by default.

### direnv

To manage environment variables, we recommend [direnv](https://direnv.net). This is an example of configuration of the `.envrc` to also generate a `.env` file:

```bash
#!/usr/bin/env bash

# Add here the environment for the docker container
cat <<EOF > .env
VAR1=variable1
VAR2=variable2
EOF
export $(cat .env | xargs)
```

This way you will have your environment variables available in your shell and in the docker container.
