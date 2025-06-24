# 📦 Установить зависимости через Poetry (для разработки)
install:
	poetry install

# 🧪 Прогнать тесты
test:
	poetry run pytest

# 🧪 Покрытие тестами + отчёт в формате XML
test-coverage:
	poetry run pytest --cov=shop_hopper --cov-report xml

# 🧹 Проверка линтинга
lint:
	poetry run flake8 shop_hopper

# 🔍 Проверка pyproject и зависимостей
selfcheck:
	poetry check

# 🔁 Полная проверка: синтаксис + тесты + линтинг
check: selfcheck test lint

# 🛠️ Сборка wheel/dists
build:
	poetry build

# 📦 Переустановить последний wheel локально через pipx (изолировано и безопасно)
reinstall-wheel:
	@latest_wheel=$$(ls -t dist/*.whl | head -n1); \
	if [ -z "$$latest_wheel" ]; then \
		echo "❌ No .whl file found in dist/"; \
		exit 1; \
	fi; \
	echo "📦 Installing $$latest_wheel with pipx..."; \
	pipx install --force "$$latest_wheel"

# 🔁 Альяс для reinstall-wheel — удобен при разработке
publish-local: reinstall-wheel

# 🗑️ Удалить установленный через pipx shop-hopper
uninstall-cli:
	pipx uninstall shop-hopper

# 🚀 Запуск с аргументами (пример: make run ARGS="'Мастер и Маргарита' -o out")
run:
	poetry run python3 -m shop_hopper.scripts.app $(ARGS)

# 🌐 Установка последней версии с GitHub через pipx (как CLI)
install-from-git:
	@GIT_URL=https://github.com/paalso/shop_hopper.git; \
	echo "🌐 Installing Shop Hopper from $$GIT_URL via pipx..."; \
	pipx install --force "$$GIT_URL"

.PHONY: install test test-coverage lint selfcheck check build reinstall-wheel publish-local run install-from-git
