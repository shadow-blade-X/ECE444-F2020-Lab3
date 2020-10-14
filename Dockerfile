FROM debian:latest
FROM python:3.7.7
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /ECE444-F2020-Lab3
WORKDIR /ECE444-F2020-Lab3
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["Hello.py"]