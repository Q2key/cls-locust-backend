clean:
	sudo rm -rf venv
install:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt
silent:
	. venv/bin/activate && locust --config=.conf --headless
ui:
	. venv/bin/activate && locust --config=.conf

.PHONY: install silent ui
