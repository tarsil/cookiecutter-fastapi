# FastAPI Cookiecutter with Tortoise ORM, Redis, Docker and Postgres.

Comes with some pre-built routes, paths, apps and [Tortoise ORM](https://tortoise.github.io/_modules/tortoise/fields/data.html)
integrated.

This project also bring a default AbstractUser (like) django where
it allows the creation of a superuser and a normal user like django as well.

![CI](https://github.com/tarsil/cookiecutter-fastapi/actions/workflows/main.yml/badge.svg)

- The requirements are in `requirements.txt` and you can locally run `make requirements`.
  It will install the dev requirements as well.
- Uses cookiecutter to generate the template project
- [FastAPI](https://fastapi.tiangolo.com/) is used for the tests with [pytest](https://docs.pytest.org/en/latest/)

---

## Table of Contents

- [FastAPI Cookiecutter with Tortoise ORM, Redis, Docker and Postgres.](#fastapi-cookiecutter-with-tortoise-orm-redis-docker-and-postgres)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [How to install](#how-to-install)

---

## Overview

This is a simple boilerplate that helps spinning up fastapi apps for your own use cases.

## Requirements

- Python 3.8 or above
- (Optional) Virtualenv (or pyenv, venv...)
- [Python Web Extras](https://github.com/tarsil/python-web-extras)
- Cookiecutter (to install the template)

## How to install

1. [Install cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
2. Run `cookiecutter https://github.com/tarsil/cookiecutter-fastapi` and follow the instructions.

The remaining instructions are inside the generated README.md of the project.
