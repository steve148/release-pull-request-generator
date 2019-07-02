include .makefile.inc

.PHONY: help
help: ##  List all available commands.
	${SHOW_IDENTITY}
	@echo 'Usage:'
	@echo '${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@perl -ne "$${HELP_SCRIPT}" $(MAKEFILE_LIST)

.PHONY: tests
tests: ##  Run the unit tests against the project.
	pipenv run python -m unittest discover -s tests/

.PHONY: lint
lint: ##  Run linter checks against the project.
	pipenv run flake8 **/*.py