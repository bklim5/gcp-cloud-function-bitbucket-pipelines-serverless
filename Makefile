SOURCES = $(shell find . -name "*.py")

install:
	pip install -r requirements.txt

install-dev: install
	pip install -r requirements-test.txt

lint:
	flake8 app tests

test:
	ENVIRONMENT_NAME=test PYTHONPATH=./app:. pytest -sv tests/

coverage:
	ENVIRONMENT_NAME=test PYTHONPATH=./app:. pytest tests/ --cov=app

linttest: lint test
