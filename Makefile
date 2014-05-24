MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_angular_backend.settings $(MANAGE) test hello

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_angular_backend.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_angular_backend.settings $(MANAGE) syncdb --noinput
