# Follow the guideline to run docker based jupyter notebook
```bash
$ docker run -it --name jupyter-data1 -p 8888:8888 -v ${PWD}:/home/jovyan/work -e JUPYTER_ENABLE_LAB=yes jupyter/datascience-notebook
```

- After first run and stopping the container:
```bash
$ docker start -ia jupyter-data1
```

