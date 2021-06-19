.PHONY: lint format test

lint:
	poetry run black --check --diff --color .
	poetry run isort --check --diff --color .
	poetry run flake8 .

format:
	poetry run black .
	poetry run isort .

test:
	poetry run coverage run -m unittest
	poetry run coverage xml
