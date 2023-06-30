.PHONY: run-server
run-server:
	python manage.py runserver 8001

.PHONY: migrate
migrate:
	python manage.py migrate

