VENV_PATH := $(HOME)/venv/bin
PROJ_NAME := aiochat

runserver:
	$(VENV_PATH)/python $(PROJ_NAME)/app.py

start:
	mkdir -p var
	$(VENV_PATH)/gunicorn --preload --pid var/gunicorn.pid \
		-D -b 127.0.0.1:8000 $(PROJ_NAME).wsgi:app \
		--worker-class $(VENV_PATH)/aiohttp.worker.GunicornWebWorker

stop:
	kill `cat var/gunicorn.pid` || true

restart: stop start

pep8:
	$(VENV_PATH)/pep8 --exclude=*migrations*,*settings_local.py* \
		--max-line-length=119 --show-source  $(PROJ_NAME)/

pyflakes:
	$(VENV_PATH)/pylama --skip=*migrations* -l pyflakes $(PROJ_NAME)/

lint: pep8 pyflakes

test:
	$(VENV_PATH)/nosetests --rednose --force-color aiochat

cover_test:
	$(VENV_PATH)/nosetests --rednose --force-color --with-coverage --cover-min-percentage=90 aiochat

cover_report:
	$(VENV_PATH)/coverage html
	$(VENV_PATH)/coverage-badge > htmlcov/coverage.svg

ci_test: cover_test cover_report lint

wheel_install:
	$(VENV_PATH)/pip install --no-index -f wheels/ -r requirements.txt
