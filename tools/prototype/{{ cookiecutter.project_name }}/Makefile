.DEFAULT_GOAL := help

PROJECT_NAME = {{ cookiecutter.project_name }}
AWS_REGION ?= eu-central-1
AWS_ACCOUNT ?=
AWS_PROFILE ?=
AWS_DOMAIN ?=

ECR = $(AWS_ACCOUNT).dkr.ecr.$(AWS_REGION).amazonaws.com
DOCKER_IMAGE ?= $(ECR)/$(PROJECT_NAME)
DOCKER_NETWORK ?= host
ENV_FILE ?= .env
LOCAL_ENV_FILE ?= .envrc
LOCAL_ETL_DIR ?= $(shell pwd)

DOCKER_TAG ?= latest
DOCKER_DEV_TAG ?= dev


.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'


.tmp: # Create tmp directory.
	@mkdir -p tmp/data


.env:  # Create .env files.
	@touch ${ENV_FILE}
	@touch ${LOCAL_ENV_FILE}
	@echo "CONFIG_FILE=config.yml" > ${ENV_FILE}
	@echo "PYTHONPATH=src" >> ${ENV_FILE}
	#@echo "CODEARTIFACT_AUTH_TOKEN=`aws codeartifact get-authorization-token --domain $(AWS_DOMAIN) --domain-owner $(AWS_ACCOUNT) --query authorizationToken --output text --profile $(AWS_PROFILE)`" >> ${ENV_FILE}
	@echo "#!/bin/sh" > ${LOCAL_ENV_FILE}
	@echo "dotenv" >> ${LOCAL_ENV_FILE}
	@direnv allow .


.PHONY: clean
clean:  ## Delete Python binaries.
	@find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete


.PHONY: .ecr_login
.ecr_login:  # Login to ECR.
	@aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin https://$(AWS_ACCOUNT).dkr.ecr.$(AWS_REGION).amazonaws.com


.PHONY: .install
.install: .env .tmp


.PHONY: build
build: .install  ## Build local image with DOCKER_TAG.
	@docker build -f ../../../docker/default.dockerfile \
		--build-arg PROJECT_PATH=packages/apps/{{ cookiecutter.project_name }}\
		--build-arg CODEARTIFACT_AUTH_TOKEN="${CODEARTIFACT_AUTH_TOKEN}"\
		--build-arg PIPENV_OPTIONS="" \
		-t $(DOCKER_IMAGE):$(DOCKER_TAG) ../../../


.PHONY: build-dev
build-dev: .install  ## Build local image with DOCKER_DEV_TAG.
	@docker build -f ../../../docker/default.dockerfile \
		--build-arg PROJECT_PATH=packages/apps/{{ cookiecutter.project_name }}\
		--build-arg CODEARTIFACT_AUTH_TOKEN="${CODEARTIFACT_AUTH_TOKEN}"\
		--build-arg PIPENV_OPTIONS="--dev" \
		-t $(DOCKER_IMAGE):$(DOCKER_TAG) ../../../


.PHONY: run
run: .install  ## Run remote image.
	@docker run  \
		--name=$(PROJECT_NAME)\
		--network=${DOCKER_NETWORK} \
		--env-file ${ENV_FILE}\
		-v ${LOCAL_ETL_DIR}:/opt/project \
		-v ${HOME}/.aws/credentials:/root/.aws/credentials:ro \
		-v ${HOME}/.aws/config:/root/.aws/config:ro \
		--rm $(DOCKER_IMAGE):$(DOCKER_TAG)


.PHONY: run-it
run-it: .install  ## Get into remote image.
	@docker run  -it \
		--name=$(PROJECT_NAME)\
		--network=${DOCKER_NETWORK} \
		--env-file ${ENV_FILE}\
		-v ${LOCAL_ETL_DIR}:/opt/project \
		-v ${HOME}/.aws/credentials:/root/.aws/credentials:ro \
		-v ${HOME}/.aws/config:/root/.aws/config:ro \
		--rm $(DOCKER_IMAGE):$(DOCKER_TAG) bash


.PHONY: test
test: .install   ## Locally run tests.
	@PYTHONPATH=src PIPENV_VERBOSITY=-1 poetry run pytest --cov=$(PROJECT_NAME) -v tests/
	@PIPENV_VERBOSITY=-1 poetry run coverage html


.PHONY: pre-commit
pre-commit: ## Force execution of pre-commit hooks
	@PIPENV_VERBOSITY=-1 pre-commit run --all-files


.PHONY: renew_codeartifact_token
renew_codeartifact_token: ## Set a new AWS codeartifact token in the .env environment variable CODEARTIFACT_AUTH_TOKEN.
	@grep -v CODEARTIFACT_AUTH_TOKEN ${ENV_FILE} > _${ENV_FILE}
	@echo "CODEARTIFACT_AUTH_TOKEN=`aws codeartifact get-authorization-token --domain $(AWS_DOMAIN) --domain-owner $(AWS_ACCOUNT) --query authorizationToken --output text --profile $(AWS_PROFILE)`" >> _${ENV_FILE}
	@mv _${ENV_FILE} ${ENV_FILE}
	@direnv allow .
