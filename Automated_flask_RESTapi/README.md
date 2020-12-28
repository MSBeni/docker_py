# Our goal here is to create an automated container image built process which creates an image implementing microservice instance waiting for HTTP request at port 5000  
```bash
$ docker pull jupyter/tensorflow-notebook
```

- run the container:
```bash
$ docker run -d --name temp jupyter/tensorflow-notebook
```

- installing Torch:
```bash
$ docker exec -it temp pip install torch torchvision
```

- stop container:
```bash
$ docker stop temp
```

- run jupyter container:
```bash
$ docker run -it --rm -p 8888:8888 -v ${PWD}:/home/jovyan/notebooks myjupyter:torch
```

- remove container:
```bash
$ docker rm temp
```