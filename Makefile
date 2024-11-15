install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=shop_hopper --cov-report xml

lint:
	poetry run flake8 shop_hopper

selfcheck:
	poetry check

check: selfcheck test lint

build:
	poetry build

# make run ARGS="'Физика Ландсберг' -o tmp_dir"
run:
	poetry run python3 -m shop_hopper.scripts.app $(ARGS)

.PHONY: install test lint selfcheck check build
