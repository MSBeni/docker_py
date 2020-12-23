# Follow the guideline to run docker based Django simple application
```bash
$ docker run -it --name mydjango1 -p 8000:8000 -v ${PWD}:/app python:3.8 bash
```
On container bash terminal:
```bash
$ pip install Django==3.1.4
$ cd app/
$ django-admin startproject testsite
$ cd testsite/
$ python manage.py runserver 0:8000
```

# Follow the guideline to run docker based Flask simple application

