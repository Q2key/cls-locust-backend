VENV_FOLDER=venv
PYTHON=$(VENV_FOLDER)/bin/python3

clean:
	sudo rm -rf $(VENV_FOLDER)
install:
	python3 -m venv $(VENV_FOLDER)
	$(PYTHON) -m pip install -r requirements.txt
silent:
	$(PYTHON) -m locust --config=.conf --headless
ui:
	$(PYTHON) -m locust --config=.conf
reinstall: clean install

.PHONY:clean install silent ui reinstall
