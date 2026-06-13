# svc-orders — developer makefile
# Targets are intentionally minimal; CI runs `make ci`.

PYTHON ?= python3

.PHONY: codegen lint mypy test ci clean help

help:
	@echo "Targets:"
	@echo "  codegen   Regenerate codegen/ from schema/*.yaml"
	@echo "  lint      Run ruff on src/ codegen/ tests/ tools/"
	@echo "  mypy      Run mypy on src/ codegen/"
	@echo "  test      Run pytest"
	@echo "  ci        codegen + lint + mypy + test"

codegen:
	$(PYTHON) tools/codegen.py

lint:
	cd $(CURDIR) && ruff check src codegen tests tools

mypy:
	cd $(CURDIR) && mypy src codegen

test:
	cd $(CURDIR) && pytest -q

ci: codegen lint mypy test
	@echo "ci passed"

clean:
	rm -rf .ruff_cache .mypy_cache .pytest_cache
