.PHONY: lint mypy black flake

POETRY ?= $(shell command -v poetry 2> /dev/null)

black:
	$(POETRY) run black .

flake:
	$(POETRY) run flakeheaven lint

mypy:
	$(POETRY) run mypy .

lint: black flake mypy
