lint:
	poetry run black --check --diff --color .
	poetry run isort --check --diff --color .
	poetry run flake8 .

format:
	poetry run black .
	poetry run isort .
