# BJSS_liveobs_automation
Automation Test Suite for LiveObs

# Running locally
1. Modify the `config.yml` parameters such as database and server URL 
to ensure they are correct for your local instance.
2. Run Chromedriver.exe in a terminal.
3. Start your local LiveObs server.
4. Run Behave.
	1. Create a Behave run configuration in PyCharm.
	2. Populate the 'feature files or folders' field.

# Running on GoCD
Use the Makefile targets.