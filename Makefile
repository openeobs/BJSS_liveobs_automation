#!/usr/bin/make

install:
	virtualenv venv
	venv/bin/pip install -r requirements.txt

install_chromedriver:
	curl -o chromedriver.zip -SL https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip
	unzip -d chromedriver chromedriver.zip
	rm chromedriver.zip

run: install_chromedriver
	PATH=$$PATH:chromedriver/ venv/bin/behave features/

.PHONY: install run install_chromedriver
