.PHONY: lint format test

lint:
	poetry run black --check --diff --color .
	poetry run isort --check --diff --color .
	poetry run flake8 .

format:
	poetry run black .
	poetry run isort .

test:
	python main.py setup
	poetry run coverage run -m unittest
	python main.py teardown
	poetry run coverage xml
