.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: clean_pyc ## Clean all PYC in the system

.PHONY: clean_pyc
clean_pyc: ## Cleans all *.pyc in the system
	find . -type f -name "*.pyc" -delete || true

.PHONY: requirements
requirements: ## Installs the requirements
	pip install -r requirements/requirements.txt

.PHONY: requirements-dev
requirements-dev: ## Installs the requirements for development
	pip install -r requirements/requirements-dev.txt

.PHONY: serve
serve: ## Starts the local server
	FASTAPI_SETTINGS_MODULE='core.configs.development.settings' python {{ cookiecutter.project_src_name }}/serve.py

.PHONY: serve-special
serve-special: ## Starts the server by passing a special settings file `FLASK_SETTINGS_FILENAME`
	FASTAPI_SETTINGS_MODULE=$(FASTAPI_SETTINGS_MODULE) python {{ cookiecutter.project_src_name }}/serve.py

.PHONY: run-tests
run-tests: ## Runs the local tests with nose
	FASTAPI_SETTINGS_MODULE='core.configs.testing.settings' nosetests --exe --with-specplugin
