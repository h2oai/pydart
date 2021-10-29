setup: setup-docs

clean: clean-docs

setup-docs:
	mkdir -p tools/docs && cd tools/docs && python3 -m venv venv
	./tools/docs/venv/bin/python -m pip install --upgrade pip mkdocs-material

serve-docs:
	./tools/docs/venv/bin/mkdocs serve

.PHONY: docs
docs:
	./tools/docs/venv/bin/mkdocs build

clean-docs:
	rm -rf tools/docs/venv

