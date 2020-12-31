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


