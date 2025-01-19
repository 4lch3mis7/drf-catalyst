.PHONY: startproject


startproject:
	# Rename the project
	mv drf_catalyst $(PROJECT_NAME)
	mv ../drf-catalyst ../$(PROJECT_NAME) && cd ../$(PROJECT_NAME)

	# Replace project name in files
	find . -type f -exec sed -i 's/drf_catalyst/$(PROJECT_NAME)/g' {} \;
	find . -type f -exec sed -i 's/drf-catalyst/$(PROJECT_NAME)/g' {} \;

	# Set up the environment
	cp .env.dist .env

