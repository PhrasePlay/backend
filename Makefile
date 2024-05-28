SUPERUSER_NAME=admin
SUPERUSER_EMAIL=admin@example.com
SUPERUSER_PASSWORD=admin

down:
	docker-compose down -v

build:
	docker-compose build --no-cache

up:
	docker-compose up -d

migrate:
	docker-compose run web python manage.py migrate

createsuperuser:
	docker-compose run web python manage.py createsuperuser --noinput || true
	@docker-compose run web python manage.py shell -c " \
	from django.contrib.auth import get_user_model; \
	User = get_user_model(); \
	if not User.objects.filter(username='$(SUPERUSER_NAME)').exists(): \
		User.objects.create_superuser('$(SUPERUSER_NAME)', '$(SUPERUSER_EMAIL)', '$(SUPERUSER_PASSWORD)');"

full-setup: down build up migrate createsuperuser
