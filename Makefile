.PHONY: lint

lint:
	python3 -m black .
	python3 -m flakeheaven lint
	python3 -m mypy .