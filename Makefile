
headles:
	locust --config=.conf --headless
run:
	locust --config=.conf
.PHONY:run
