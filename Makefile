clean:
	find . -name "*.pyc" -exec rm -rf {} \;

run: clean
	python manage.py runserver

migrate: clean
	python manage.py migrate

migrations: clean
	python manage.py makemigrations

exclude_migrations: clean
	rm **/migrations/*[0-9]*.py

superuser: clean
	python manage.py createsuperuser

shell: clean
	python manage.py shell

run_rede: clean
	./manage.py runserver 0.0.0.0:8000
