.PHONY: run \
		shell \
		mdb \
		db \
		up\


PIP_VERSION = 22.0.4

requirements: venv/bin/activate ## install requirements
	/venv/bin/activate; pip install -r requirements.txt


run: venv/bin/activate ## Local Run
	/venv/bin/activate; python coolsite/manage.py runserver

shell: venv/bin/activate ## Run django shell
	/venv/bin/activate; python coolsite/manage.py shell


mdb: venv/bin/activate ## Make migrations
	/venv/bin/activate; python coolsite/manage.py makemigrations

db: venv/bin/activate ## Migrate to database
	/venv/bin/activate; python coolsite/manage.py migrate

up: venv/bin/activate ## create or up docker-compose container
	/venv/bin/activate; docker-compose up

web.shell: venv/bin/activate ## enter docker-compose Django app service shell
	/venv/bin/activate; docker-compose exec web /bin/sh

web.db: venv/bin/activate ## migrate changes to db container
	/venv/bin/activate; docker-compose exec web python coolsite/manage.py migrate

web.user: venv/bin/activate ## create superuser in django app docker-compose service
	/venv/bin/activate; docker-compose exec web python coolsite/manage.py createsuperuser
