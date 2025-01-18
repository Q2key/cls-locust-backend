# locust-swarm

`locust-swarm` is a project for load testing using Locust. This README covers how to set up a virtual environment and run the project using the provided `Makefile`.

## Prerequisites

Before getting started, ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Make](https://www.gnu.org/software/make/)

Important!
You need to create .conf file (take a look at the .conf.example) and fill the variables (for now you have to set up only the API HOST)

### Using GNU Make (easiest way for MacOS, Linux and other \*nix family users)

```shell
make install
make ui

#or for silent mode (without ui)
make silent
```

### Without make (windows)

```Shell
# activate venv
python3 -m venv venv
. venv/bin/activate

# install deps

pip3 install -r requirements.txt

#run locust
locust --config=.conf
```

