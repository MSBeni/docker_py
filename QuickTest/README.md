# Follow the guideline to run docker based Django simple application
```bash
$ docker run -it --name mydjango1 -p 8000:8000 -v ${PWD}:/app python:3.8 bash
```
On container bash terminal:
```bash
# pip install Django==3.1.4
# cd app/
# django-admin startproject testsite
# cd testsite/
# python manage.py runserver 0:8000
# exit
```

# Follow the guideline to run docker based Flask simple application
```bash
$ docker run -it --name myflask1 -p 5000:5000 -v ${PWD}:/app python:3.7 bash
```
On container bash terminal:
```bash
# pip install flask==1.1.1
# cd /app
# export FLASK_APP=Basic_Flask_App.py
# export FLASK_DEBUG=1
# flask run --host=0.0.0.0
# exit
``` 


