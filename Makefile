activate:
	source venv/bin/activate

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations

start_redis:
	brew services start redis

stop_redis:
	brew services stop redis

start_flower:
	celery -A a_core.celery_app flower

auth_flower:
	celery -A a_core.celery_app flower --basic_auth=admin:flower123

collectstatic:
	python manage.py collectstatic --noinput

celery_worker:
	celery -A a_core worker -E -l info

celery_beat:
	celery -A a_core beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

runserver:
	python manage.py runserver 9000