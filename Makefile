.PHONY: requirements\
		run \
		shell \
		mdb \
		db \


PIP_VERSION = 22.0.4

help: ## Show available make targets and their descriptions
	@echo "Available make targets:"
	@echo ""
	@awk 'BEGIN {FS = ":.*?## "}; /^[\$$\(\)\/\.0-9A-Za-z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

requirements: venv/bin/activate ## install requirements
	/venv/bin/activate; pip install -r requirements.txt


run: venv/bin/activate ## Local Run
	. venv/bin/activate; python coolsite/manage.py runserver

shell: venv/bin/activate ## Run django shell
	. venv/bin/activate; python coolsite/manage.py shell


mdb: venv/bin/activate ## Make migrations
	. venv/bin/activate; python coolsite/manage.py makemigrations


db: venv/bin/activate ## Migrate to database
	. venv/bin/activate; python coolsite/manage.py migrate

