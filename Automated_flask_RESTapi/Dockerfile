FROM  python:3
WORKDIR /app
COPY ./app .
RUN pip install -r requirements.txt
ENV FLASK_NEW development
EXPOSE 5000
CMD ["python", "color_boxes.py"]