
.PHONY: run
run: 
	( \
       . venv/bin/activate; \
       python3 app/manage.py runserver; \
	)	
build: 
	( \
       . venv/bin/activate; \
       python3 app/manage.py makemigrations; \
       python3 app/manage.py migrate; \
       python3 app/manage.py runserver; \
	)	
docker:
	sudo docker-compose build
	sudo docker-compose up
