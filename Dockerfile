FROM bitnami/python:3.11.9-debian-12-r23 

COPY requirements.txt requirements.txt

RUN python3.11 -m pip install -r requirements.txt

#RUN mkdir /app

WORKDIR /app

ENTRYPOINT [ "tail" ]