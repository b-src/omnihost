.PHONY: lint mypy black flake

POETRY ?= $(shell command -v poetry 2> /dev/null)

BLACK_ARGS ?= .
black:
	$(POETRY) run black $(BLACK_ARGS)

BLACK_ARGS ?= lint
flake:
	$(POETRY) run flakeheaven $(FLAKE_ARGS)

MYPY_ARGS ?= .
mypy:
	$(POETRY) run mypy $(MYPY_ARGS)

lint: black flake mypy
