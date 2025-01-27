.PHONY: all refactor env clean

SHELL = /bin/bash
PROJECT_NAME = $(shell basename $(shell pwd) | tr '-' '_' | tr '[:upper:]' '[:lower:]')

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
	rm README.md
	rm -rf .github/
	rm -rf .git/	
