# locust-swarm

`locust-swarm` is a project for load testing using Locust. This README covers how to set up a virtual environment and run the project using the provided `Makefile`.

## Prerequisites

Before getting started, ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Make](https://www.gnu.org/software/make/)

## Setting up the environment

1. **Create a virtual environment**: It is recommended to use a Python virtual environment to keep dependencies isolated.

   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```
2. **Setup Environments**: Create .conf file and set up the api host
   ```code
   # url example
   host = http://localhost:5114/api
   
3. **Run locust** 
    ```bash
   make ui #run locust with ui
   make headless #run locust in headless mode
    ```

### Makefile install (optional)
1. make install
2. make ui #ui mode
3. make silent #headless mode