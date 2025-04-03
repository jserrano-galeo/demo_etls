.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: pre-commit
pre-commit:   ## Configure pre-commit hooks locally.
	@echo "Installing pre-commit hooks"
	PIPENV_VERBOSITY=-1 pre-commit install
	@echo "Running pre-commit for the whole project"
	PIPENV_VERBOSITY=-1 pre-commit run -a
	@echo "Done"

.PHONY: new-etl
new-etl:
	@cookiecutter ./tools/prototype --output-dir ./packages/services
