# Our goal here is to create an automated container image built process which creates an image implementing microservice instance waiting for HTTP request at port 5000.
simply run this command to build the container: 
```bash
$ docker build -t cb:simple -f Dockerfile .
```

Now run the container:
```bash
$ docker run -it --rm -p 5000:5000 cb:simple
```

- In order to test the ARGs used to build the Dockerfile completing the FROM, please check the from.Dockerfile and run this command:
```bash
$ docker build -t cb:from -f from.Dockerfile --build-arg tag=3.8 .
```

- Now run the container:
```bash
$ docker run --rm cb:from cat /tmp/base_img
```
```bash
$ docker run --rm -p 5000:5000 cb:from
```

You can also test other Dockerfiles indicating other similar approaches. Finally, the final complete Dockerfile will be run.
Run this command to build the container:
```bash
$ docker build -t cb:prod -f production.Dockerfile .
```
Then specify a volume to set database to store app data:
```bash
$ docker volume create cb_data
```
Then run the container using this command:
```bash
$ docker run -d --name cb -v cb_data:/data -p 5000:5000 cb:prod
```
Check the running containers simply by the command:
```bash
$ docker ps
```
You can use the Postman, Talend API or similar application to test this RESTful API. 
In this api, the database is safely stored in persistent volume, and after removing the docker container the api data will remain. Just try this step and check the api.

After loging to your docker hub account by this command:
```bash
$ docker login
```
you can tag this image and push it to your docker hub:
Renaming and Tagging:
```bash
$ docker tag cb:prod msbeni/flaskrest:0.1
```
Pushing to docker hub:
```bash
$ docker push msbeni/flaskrest:0.1
```
