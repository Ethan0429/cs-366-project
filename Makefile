up: Dockerfile docker-compose.yml .dockerignore
	docker-compose up -d

# rebuild docker image
Dockerfile:
	docker-compose build

.dockerignore:
	docker-compose build

docker-compose.yml:
	docker-compose down

down:
	docker-compose down

clean:
	docker-compose down --rmi all --volumes && rm -rf db_data/*

start: app.py
	flask run