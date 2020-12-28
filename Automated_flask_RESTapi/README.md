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