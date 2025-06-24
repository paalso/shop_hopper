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

# 📦 Reinstall the latest built wheel locally using pip (force overwrite)
reinstall-wheel:
	@latest_wheel=$$(ls -t dist/*.whl | head -n1); \
	if [ -z "$$latest_wheel" ]; then \
		echo "❌ No .whl file found in dist/"; \
		exit 1; \
	fi; \
	echo "📦 Installing $$latest_wheel..."; \
	python3 -m pip install --break-system-packages "$$latest_wheel"

# Alias for reinstall-wheel — useful for local development
publish-local: reinstall-wheel

# make run ARGS="'Физика Ландсберг' -o tmp_dir"
run:
	poetry run python3 -m shop_hopper.scripts.app $(ARGS)

.PHONY: install test lint selfcheck check build
