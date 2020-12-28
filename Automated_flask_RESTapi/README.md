# Our goal here is to create an automated container image built process which creates an image implementing microservice instance waiting for HTTP request at port 5000.
simply run this command to build the container: 
```bash
$ docker build -t cb:simple -f Dockerfile .
```

- Now run the container:
```bash
$ docker run -it --rm -p 5000:5000 cb:simple
```

