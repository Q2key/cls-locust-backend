silent:
	locust --config=.conf --headless
ui:
	locust --config=.conf

.PHONY:install silent ui
