# {{ cookiecutter.description }} - {{ cookiecutter.project_name }}

[![CircleCI](https://circleci.com/gh/tarsil/cookiecutter-flask.svg?style=shield&circle-token=dc7b04e09667d387047c4b59faa604a22867189b)](https://circleci.com/gh/tarsil/cookiecutter-flask)

- The requirements are located in `requirements.txt` and you can locally run `make requirements`. 
It will install the dev requirements as well.
- Uses cookiecutter to generate the template project
- [FastAPI](https://fastapi.tiangolo.com/) is used for the tests with [nose](https://nose.readthedocs.io/en/latest/)

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

This is a simple boierplate that helps spinning up flask microservices for your own use cases.
This aims to help you not spending a lot of hours making initial configurations for flask microservices.

## Requirements

- Python 3.8 or above
- (Optional) Virtualenv (or pyenv, venv...)
- Cookiecutter (to install the template)

## Optional Requirements

- Docker (optional and latest) and docker-compose (also optional and latest) if you want to start
a redis and postgres container and to `make run docker` working properly.

## Dependencies

- [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
- [Flask-RESTplus](https://flask-restplus.readthedocs.io/en/stable/)
- [flask-seasurf](https://flask-seasurf.readthedocs.io/en/latest/)

Also contains additional packages in case of using redis and postges by using

- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Marshmallow-SQLalchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Redis](https://redislabs.com/lp/python-redis/)

## How to install

 1. Install cookiecutter. Instructions [here](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
 2. Run `cookiecutter https://github.com/tiagoarasilva/cookiecutter-flask` and follow the instructions
 3. `make requirements` - Installs all the requirements needed.

## Development

- The template offers a possibility to integrate with redis and postgres both locally and remotely, 
where remotely is up to the developer.
    1. Locally run `docker-compose up` and the service should trigger normally
    2. Remotely, replace settings (`config/settings.py`) with the settings you need

- If you wish to have other databases, just replace the variables by the ones necessary

## Run locally

- make run-local` or if you wish to run with a different set of settings:
    1. `make run-special FLASK_SETTINGS_FILENAME=_location_of_file/file.py`

- You should be able to access `http://127.0.0.1:5001/` and test the endpoint.

## Configurations

The project comes with pre-set of configurations located at `src/config/`.

 1. `settings.py` is the main default settings config.

Inside the config module contains the `development` and `testing` modules but those can
be overwritten, removed or moved to a different location and easily called by the 
`FLASK_SETTINGS_FILENAME` environment variable.

## Run tests

- `make run-tests` - Runs all the standard tests
- `make run-nose` - Runs all the tests inside the tests module and app
