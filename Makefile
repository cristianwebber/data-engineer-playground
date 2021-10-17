export SHELL:=/bin/bash
export SHELLOPTS:=$(if $(SHELLOPTS),$(SHELLOPTS):)pipefail:errexit

.ONESHELL:

venv:
	test -d venv || python3 -m venv venv
	. venv/bin/activate
	pip install pre-commit