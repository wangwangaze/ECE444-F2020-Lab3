FROM ubuntu:14.04
FROM python:3.7.5-slim
RUN apt-get update -y
RUN apt-get install -y python-pip
RUN apt-get install -y python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]