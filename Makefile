.PHONY: startproject


startproject:
	mv drf_catalyst $(PROJECT_NAME)
	sed -i 's/drf_catalyst/$(PROJECT_NAME)/g' manage.py
	sed -i 's/drf_catalyst/$(PROJECT_NAME)/g' $(PROJECT_NAME)/settings.py 
