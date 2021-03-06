# {{ cookiecutter.description }} - {{ cookiecutter.project_name }}

[![CircleCI](https://circleci.com/gh/tarsil/cookiecutter-fastapi.svg?style=shield&circle-token=d87aa2df60aa0ad7674625af40fb78bf954349af)](https://circleci.com/gh/tarsil/cookiecutter-fastapi)

- The requirements are located in `requirements.txt` and you can locally run `make requirements`.
It will install the dev requirements as well.
- Uses cookiecutter to generate the template project
- [FastAPI](https://fastapi.tiangolo.com/) is used for the tests with [nose](https://nose.readthedocs.io/en/latest/)

---

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Optional Requirements](#optional-requirements)
- [How to install](#how-to-install)


---

## Overview

This is a simple boilerplate that helps spinning up fastapi apps for your own use cases.

## Requirements

- Python 3.8 or above
- (Optional) Virtualenv (or pyenv, venv...)
- Cookiecutter (to install the template)

## How to install

 1. [Install cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
 2. Run `cookiecutter https://github.com/tarsil/cookiecutter-fastapi` and follow the instructions.
 3. `make requirements` - Installs all the requirements needed.

The remaining instructions are inside the generated README.md of the project.
