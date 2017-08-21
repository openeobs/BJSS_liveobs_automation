#!/usr/bin/make
install_sauce_connect:
	curl -o sauce_connect.tar.gz -SL https://saucelabs.com/downloads/sc-4.4.9-linux.tar.gz
	tar -xf sauce_connect.tar.gz
	rm sauce_connect.tar.gz
	mv sc-4.4.9-linux sauce_connect

run_sauce_connect:
	test -f /var/tmp/sc.pid && kill -9 $(cat /var/tmp/sc.pid)
	(nohup sauce_connect/bin/sc \
		-u ${SAUCELABS_USERNAME} \
		-k ${SAUCELABS_ACCESS_TOKEN} \
		-l sauce_connect.log \
		-i ${GO_REVISION_LIVEOBS} \
		--pidfile /var/tmp/sc.pid &)
	sleep 30

install:
	virtualenv venv
	venv/bin/pip install -r requirements.txt

install_chromedriver:
	curl -o chromedriver.zip -SL https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip
	unzip -d chromedriver chromedriver.zip
	rm chromedriver.zip

run: install_chromedriver
	curl http://localhost:8069/web
	sleep 15
	PATH=$$PATH:chromedriver/ venv/bin/behave features/

.PHONY: install run install_chromedriver install_sauce_connect run_sauce_connect
