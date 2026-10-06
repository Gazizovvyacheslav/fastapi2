build:
	docker build -t fastapi_2_project .
	docker run -d --name fastapi_run1 -p 127.0.0.1:8001:8000 fastapi_2_project

start:
	docker start fastapi_run1

stop:
	docker stop fastapi_run1
	docker rm fastapi_run1
	docker rmi fastapi_2_project

logs:
	docker logs -f fastapi_run1