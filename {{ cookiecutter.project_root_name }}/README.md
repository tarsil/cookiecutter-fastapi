# {{ cookiecutter.description }} - {{ cookiecutter.project_name }}

- The requirements are located in `requirements.txt` and you can locally run `make requirements`.
It will install the dev requirements as well.
- Uses cookiecutter to generate the template project
- [FastAPI](https://fastapi.tiangolo.com/) is used for the tests with [pytest](https://docs.pytest.org/en/latest/)

---

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Optional Requirements](#optional-requirements)
- [Dependencies](#dependencies)
- [How to install](#how-to-install)
- [Development](#development)
- [Run Locally](#run-locally)
- [Configurations](#configurations)
- [Run Tests](#run-tests)

---

## Overview

This is a simple boilerplate that helps spinning up fastapi apps for your own use cases.

## Requirements

- Python 3.8 or above
- (Optional) Virtualenv (or pyenv, venv...)
- Cookiecutter (to install the template)

## How to install

 1. Install cookiecutter. Instructions [here](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
 2. Run `cookiecutter https://github.com/tarsil/cookiecutter-fastapi` and follow the instructions.
 3. `make requirements` - Installs all the requirements needed.

## Run locally

- `make run-dev` or if you wish to run with a different set of settings:
    1. `make serve-special FASTAPI_SETTINGS_MODULE=name_of_module.file`

- You should be able to access `http://127.0.0.1:8002/` and test the endpoint.

## Configurations

The project comes with pre-set of configurations located at
`{{ cookiecutter.project_root_name }}/{{ cookiecutter.project_src_name }}/core/configs/`.

 1. `settings.py` is the main default settings config.

## Run tests

- `make test` - Runs all the standard tests.
