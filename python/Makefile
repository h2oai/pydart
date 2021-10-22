all: build ## Build h2o_nitro wheel

.PHONY: build
build: clean-build
	./venv/bin/python3 setup.py bdist_wheel

setup: ## Install dependencies
	python3 -m venv venv
	./venv/bin/python -m pip install --upgrade pip
	./venv/bin/python -m pip install setuptools wheel pytest flake8
	# ./venv/bin/python -m pip install -r examples/requirements.txt
	./venv/bin/python -m pip install --editable .

.PHONY: docs
docs: ## Build API docs
	echo "not implemented"

clean-build: ## Purge previous build
	rm -rf build dist h2o_nitro.egg-info

clean: clean-build ## Clean
	rm -rf venv docs/build

help: ## List all make tasks
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

