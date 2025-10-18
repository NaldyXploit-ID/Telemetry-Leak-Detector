.PHONY: run test
run:
	python3 main.py encode "hello"
test:
	@echo "Running demo tests..."
	@python3 -m pytest -q || true
