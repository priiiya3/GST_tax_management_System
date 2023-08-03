FROM python:3.9.6-alpine

WORKDIR /GST-App

ADD . /GST-App
RUN apk add build-base
RUN pip install -r requirements.txt
EXPOSE 9696
CMD ["python","app.py"]
