.PHONY: all refactor env clean

SHELL = /bin/bash

all: refactor env clean

refactor:
	# Rename the project
	mv drf-catalyst/drf_catalyst ./$(PROJECT_NAME)
	mv drf-catalyst/* ./
	mv drf-catalyst/.* ./

	# Replace project name in files
	PROJECT_NAME="$( $(PROJECT_NAME) )"
	find . -type f -exec sed -i 's/drf_catalyst/$(PROJECT_NAME)/g' {} \;
	find . -type f -exec sed -i 's/drf-catalyst/$(PROJECT_NAME)/g' {} \;

env:
	# Set up the environment
	cp .env.dist .env

clean:
	rmdir drf-catalyst
	rm Makefile
	rm -rf .git/
