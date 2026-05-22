SHELL := /bin/bash

.PHONY: manuscript clean numbers test inventory context-pack

manuscript:
	cd manuscript && pdflatex -interaction=nonstopmode -halt-on-error main.tex && pdflatex -interaction=nonstopmode -halt-on-error main.tex && pdflatex -interaction=nonstopmode -halt-on-error main.tex

clean:
	cd manuscript && latexmk -C main.tex || true
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
	find . -name ".pytest_cache" -type d -prune -exec rm -rf {} +

numbers:
	python3 calculations/devries_spectrum.py

test:
	python3 scripts/check_project.py
	python3 -m pytest -q calculations/tests

inventory:
	python3 scripts/source_inventory_check.py

context-pack:
	python3 scripts/make_context_pack.py
