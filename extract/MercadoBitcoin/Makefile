export SHELL:=/bin/bash
export SHELLOPTS:=$(if $(SHELLOPTS),$(SHELLOPTS):)pipefail:errexit

.ONESHELL:

venv:
	test -d venv || python3 -m venv venv
	. venv/bin/activate

clean:
	rm -rf venv day-summary *.checkpoint .pytest_cache .coverage htmlcov

init: clean venv
	pip install poetry
	poetry install

test:
	poetry run python -m pytest

cov-test:
	coverage run -m pytest
	coverage html
	google-chrome htmlcov/index.html 

build-docker-image: clean
	docker build -t cristianwebber/test:0.1.0 .

run-docker-image: build-docker-image
	#docker rm -f cristianwebber/test:0.1.0 || true
	docker run -it cristianwebber/test:0.1.0 bash

## CI/CD
ci-setup:
	pip install poetry
	poetry install

ci-test:
	poetry run python -m pytest
