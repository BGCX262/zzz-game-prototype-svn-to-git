Prerequsites:

1. Python version 2.7 (Django works with any Python version from 2.4 to 2.7 (due to backwards incompatibilities in Python 3.0, Django does not currently work with Python 3.0))
2. Django version 1.3
3. Django-piston https://bitbucket.org/jespern/django-piston/wiki/Home

Aptana Project configuration:

PYTHONPATH should include path to django-piston installation

1. Debug configuration 
	manage.py runserver --noreload 127.0.0.1:7777

2. TestRun configuration
	manage.py test