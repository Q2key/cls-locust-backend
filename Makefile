clean:
	sudo rm -rf env
activate:
	. env/bin/activate
install:
	$(clean)
	python3 -m venv env
	$(activate)
	pip install -r requirements.txt
silent:
	$(activate)
	locust --config=.conf --headless
ui:
	$(activate)
	locust --config=.conf

.PHONY:install silent ui
