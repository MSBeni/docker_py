# Building a Django RESTful api using Docker Container
- In this section you can build, run and test a django REST aoi server container
Lecture Build & Run Flask REST API Server Container

- Commands:
building docker container
```bash
$ docker build -t msbeni/mydjangoapp:0.1 .
```
Create persistent volume in docker host
```bash
$ docker volume create bookmarks_db
```
pushing image into docker hub:
First connecting to loging to your docker account:
```bash
$ docker login
```
Then pushing image to docker hub:
```bash
$ docker push msbeni/mydjangoapp:0.1
```
initialize a db on this volume by running the image with volume mounted to /data:
```bash
$ docker run -it --rm -v bookmarks_db:/data msbeni/mydjangoapp:0.1 python manage.py migrate
```
creating superuser:
```bash
$ docker run -it --rm -v bookmarks_db:/data msbeni/mydjangoapp:0.1 python manage.py createsuperuser
```
running web server:
```bash
$ docker run -it --name bm -p 8000:8000 -v bookmarks_db:/data msbeni/mydjangoapp:0.1
```

```bash
$ docker run -it --rm --name dj-dev -p 8000:8000 -v ${PWD}:/app python:3 bash
```