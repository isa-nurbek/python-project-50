install:
	uv sync

run:
	uv run gendiff.scripts.gendiff --h

lint:
	uv run ruff check

ruff-fix:
	uv run ruff check --fix

build:
	uv build

package-install:
	uv tool install dist/*.whl

reinstall:
	uv tool install --force dist/*.whl

uninstall:
	uv tool uninstall hexlet-code

.PHONY: install test lint selfcheck check build package-install reinstall uninstall