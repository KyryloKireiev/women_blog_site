.PHONY: help\
		run \
		shell \
		mdb \
		db \
		web.up\
		web.stop\
		web.down\
		web.shell\
		web.db.shell\
		web.logs\
		web.db\
		web.fill_db\
		web.flush\
		web.user\
		web.def_user\
		web.install\


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

web.up: venv/bin/activate ## create and run docker-compose container
	. venv/bin/activate; docker-compose up

web.stop: venv/bin/activate ## stop docker-compose services
	. venv/bin/activate; docker-compose stop web && \
	. venv/bin/activate; docker-compose stop db

web.down: venv/bin/activate ## down docker-compose container
	. venv/bin/activate; docker-compose down

web.shell: venv/bin/activate ## enter docker-compose Django app service shell
	. venv/bin/activate && docker-compose exec web /bin/sh

web.db.shell: venv/bin/activate ## enter docker-compose psql database shell shell
	. venv/bin/activate; docker-compose exec db psql -U my_user -d my_database
	# Get all tables names:
	# SELECT table_name FROM information_schema.tables WHERE table_schema='public';

web.logs: venv/bin/activate ## enter docker-compose web service logs
	. venv/bin/activate && docker-compose logs -f web

web.db: venv/bin/activate ## migrate changes to db container
	. venv/bin/activate; docker-compose exec web python coolsite/manage.py migrate

web.fill_db: venv/bin/activate ## add test data to database in docker-compose service "psql"
	. venv/bin/activate; docker-compose exec web python coolsite/manage.py fill_db

web.flush: venv/bin/activate ## clear database in docker-compose service "psql"
	. venv/bin/activate; docker-compose exec web python coolsite/manage.py flush --noinput

web.user: venv/bin/activate ## create custom superuser in django app docker-compose service
	. venv/bin/activate; docker-compose exec web python coolsite/manage.py createsuperuser

web.def_user: venv/bin/activate ## create default superuser in django app docker-compose service
	@echo "Now you can create a superuser and access the admin panel"
	@read -p "Username: " username && \
	read -p "Email: " email && \
	read -s -p "Password: " password && \
	docker-compose exec web python coolsite/manage.py createsuperuser --noinput --username $$username --email $$email && \
	docker-compose exec web python coolsite/manage.py shell -c "from django.contrib.auth import get_user_model;\
	                     User = get_user_model(); user = User.objects.get(username='$$username'); \
	                     user.set_password('$$password'); user.save()"

web.install: venv/bin/activate ## one-click installation (create and run container, add test data to db)
	. venv/bin/activate; docker-compose up -d && \
	make web.db && \
	make web.fill_db && \
	make web.def_user && \
	make web.logs
