PYTHON ?= python3

.PHONY: test check

test:
	$(PYTHON) -m unittest discover -s tests -v

check: test
	@echo "checks passed"
