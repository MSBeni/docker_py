# Building a Django RESTful api using Docker Container
- In this section you can build, run and test a django REST aoi server container
Lecture Build & Run Flask REST API Server Container

- Commands:
building docker container
```bash
$ docker build -t msbeni/myrestapp:0.1 .
```
pushing image into docker hub:
First connecting to loging to your docker account:
```bash
$ docker login
```
Then pushing image to docker hub:
```bash
$ docker push msbeni/myrestapp:0.1
```
Running image:
```bash
$ docker run -p 5000:5000 msbeni/myrestapp:0.1
```
