# {{ cookiecutter.description }} - {{ cookiecutter.project_name }}

- The requirements are located in `requirements.txt` and you can locally run `make requirements`.
It will install the dev requirements as well.
- Uses cookiecutter to generate the template project
- [FastAPI](https://fastapi.tiangolo.com/) is used for the tests with [pytest](https://docs.pytest.org/en/latest/)

Comes with some pre-built routes, paths, apps and [Tortoise ORM](https://tortoise.github.io/_modules/tortoise/fields/data.html)
integrated.

This project also bring a default AbstractUser (like) django where
it allows the creation of a superuser and a normal user like django as well.
---

## Table of Contents

- [{{ cookiecutter.description }} - {{ cookiecutter.project_name }}](#-cookiecutterdescription-----cookiecutterproject_name-)
    - [it allows the creation of a superuser and a normal user like django as well.](#it-allows-the-creation-of-a-superuser-and-a-normal-user-like-django-as-well)
    - [Table of Contents](#table-of-contents)
    - [Overview](#overview)
    - [Requirements](#requirements)
    - [How to install](#how-to-install)
    - [Run locally](#run-locally)
    - [Configurations](#configurations)
    - [Run tests](#run-tests)

---

## Overview

This is a simple boilerplate that helps spinning up fastapi apps for your own use cases.

## Requirements

- Python 3.8 or above
- (Optional) Virtualenv (or pyenv, venv...)
- [Python Web Extras](https://github.com/tarsil/python-web-extras)
- Cookiecutter (to install the template)

## How to install

 1. Install cookiecutter. Instructions [here](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
 2. Run `cookiecutter https://github.com/tarsil/cookiecutter-fastapi` and follow the instructions.
 3. `make requirements-dev` - Installs all the requirements needed for dev.
 4. `make requirements` (No need if 3. run) - Installs all the requirements base.

## Run locally

- `make run-dev` or if you wish to run with a different set of settings:
    1. `make serve-special FASTAPI_SETTINGS_MODULE=name_of_module.file`

- You should be able to access `http://127.0.0.1:8002/` and test the endpoint.

## Configurations

The project comes with pre-set of configurations located at
`{{ cookiecutter.project_root_name }}/{{ cookiecutter.project_src_name }}/core/configs/`.

 1. `settings.py` is the main default settings config.
 2. `make migrate`. Runs the current migrations inside the `migration` folder
 3. `make` to list all the available commands for the project.

For more info about the migrations and the tool used [aerich](https://github.com/tortoise/aerich).

## Run tests

- `make test` - Runs all the standard tests.
