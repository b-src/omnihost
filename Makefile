.PHONY: lint mypy black flake

black:
	python3 -m black .

flake:
	python3 -m flakeheaven lint

mypy:
	python3 -m mypy .

lint:
	python3 -m black .
	python3 -m flakeheaven lint
	python3 -m mypy .