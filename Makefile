install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 gen_diff

test:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

test-coverage-percent:
	pytest --cov=/home/project_gendiff/python-project-50 --cov-report term-missing

rec:
	asciinema rec

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build
