# Follow the guideline to manualyy build a docker file using the jupyter base image
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