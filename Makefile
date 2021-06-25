.PHONY: lint format test

lint:
	poetry run black --check --diff --color .
	poetry run isort --check --diff --color .
	poetry run flake8 .

format:
	poetry run black .
	poetry run isort .

test:
	poetry run python main.py setup
	poetry run alembic -x target=test upgrade head
	poetry run pytest --cov=. --cov-report=xml
	poetry run python main.py teardown
