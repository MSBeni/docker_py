# Our goal here is to create a flaask RESTful API using a multi-container docker compose file
Every detail is mentioned in the docker-compose file and can be reviewed quickly. As can be seen, there are three services defined there.
First try to pull and build the base images used in this project.
To do so, simply run these commands on your terminal:
```bash
$ docker-compose pull
```
```bash
$ docker-compose build
```
Then you can build and run your project in the background using this command:
```bash
$ docker-compose up -d
```
As we are using the mariadb and it make the connection with the mysql in the other service and mariadb taked 20 to 30 seconds to setup, probabely you can see some errors by checking the logs.
to check the logs run this command:
```bash
$ docker-compose logs
```
After about 20 seconds you are good to go and check the api by testing it on the local host port 5000.
Use the Talend API tester or Postman to do so, and ingest some data into your database.
You can always run the services separately to prevent the startup errors.
To do so, please first stop all the services without removing the volumes. To do this please run:
```bash
$ docker-compose down
```
Then run the services separately:
```bash
$ docker-compose up -d db
```
and check its logs:
```bash
$ docker-compose logs db
```
Then launch the cb service separately:
```bash
$ docker-compose up -d cb
```
and check its logs:
```bash
$ docker-compose logs cb
```
and finally launch the final service:
```bash
$ docker-compose up -d phpmyadmin
```
You can check the phpmyadmin by checking you localhost (http://localhost:8080/) using the defined user and password in service db.

do not forget to stop the services when you're done testing the api.
```bash
$ docker-compose down -v
```




