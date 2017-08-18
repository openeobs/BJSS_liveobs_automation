#!/usr/bin/make

install:
	virtualenv venv
	venv/bin/pip install -r requirements.txt

setup_chromedriver:
	export PATH=$PATH:/usr/lib/chromium-browser/

run: setup_chromedriver
	venv/bin/behave features/

.PHONY: install run
