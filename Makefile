install:
	uv sync

run:
	uv run gendiff

lint:
	uv run ruff check

build:
	uv build

package-install:
	uv tool install dist/*.whl

reinstall:
	uv tool install --force dist/*.whl

uninstall:
	uv tool uninstall hexlet-code

.PHONY: install test lint selfcheck check build package-install reinstall uninstall