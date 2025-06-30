install: ## 📦 Установить зависимости через Poetry (для разработки)
	poetry install

test: ## 🧪 Прогнать тесты
	poetry run pytest

test-coverage: ## 🧪 Покрытие тестами + отчёт в формате XML
	poetry run pytest --cov=shop_hopper --cov-report xml

lint: ## 🧹 Проверка линтинга
	poetry run flake8 shop_hopper

selfcheck: ## 🔍 Проверка pyproject и зависимостей
	poetry check

check: selfcheck test lint ## 🔁 Полная проверка: синтаксис + тесты + линтинг


build: ## 🛠️ Сборка wheel/dists
	poetry build

reinstall-wheel: ## 📦 Переустановить последний wheel локально через pipx (изолировано и безопасно)
	@latest_wheel=$$(ls -t dist/*.whl | head -n1); \
	if [ -z "$$latest_wheel" ]; then \
		echo "❌ No .whl file found in dist/"; \
		exit 1; \
	fi; \
	echo "📦 Installing $$latest_wheel with pipx..."; \
	pipx install --force "$$latest_wheel"

publish-local: reinstall-wheel ## 📦 Алиас для reinstall-wheel — удобен при разработке


uninstall-cli: ## 🗑️ Удалить установленный через pipx shop-hopper
	pipx uninstall shop-hopper

run: ## 🚀 Запуск с аргументами (пример: make run ARGS="'Мастер и Маргарита' -o out")
	poetry run python3 -m shop_hopper.scripts.app $(ARGS)

install-from-git: ## 🌐 Установка последней версии с GitHub через pipx (как CLI)
	@GIT_URL=https://github.com/paalso/shop_hopper.git; \
	echo "🌐 Installing Shop Hopper from $$GIT_URL via pipx..."; \
	pipx install --force "$$GIT_URL"

help: ## 📘 Вывод всех доступных команд и описаний
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: install test test-coverage lint selfcheck check build reinstall-wheel publish-local uninstall-cli run install-from-git help
