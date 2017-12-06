FROM ubuntu:16.04

MAINTAINER Eranga Bandara (erangaeb@gmail.com)

# Update apt-get sources AND install required packages
RUN apt-get update -y
RUN apt-get install -y apt-transport-https
RUN apt-get install -y build-essential
RUN apt-get install -y python python-pip python-dev python-setuptools
RUN apt-get install -y libmysqlclient-dev

# copy app
ADD . /app
WORKDIR /app

# run app
ENTRYPOINT [ "python", "/app/crypto.py" ]
