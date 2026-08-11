.PHONY: install run test coverage analyzers

install:
	python -m pip install -r requirements-dev.txt

run:
	python run.py

test:
	python -m pytest

coverage:
	python -m pytest --cov=app --cov-branch --cov-report=term-missing

analyzers:
	python -m pip install -r tool-triggers/requirements.txt
