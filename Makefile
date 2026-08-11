.PHONY: install run test coverage lint analyzers docker-build docker-run

install:
	python -m pip install -r requirements-dev.txt

run:
	python run.py

test:
	python -m pytest

coverage:
	python -m pytest --cov=app --cov-branch --cov-report=term-missing

lint:
	ruff check app tests

analyzers:
	python -m pip install -r tool-triggers/requirements.txt

docker-build:
	docker build -t flask-web-api .

docker-run:
	docker run --rm -p 8000:8000 flask-web-api
