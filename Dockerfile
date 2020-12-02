FROM python:3.8

COPY . /python-test-jenkins

WORKDIR /python-test-jenkins

RUN pip3 install pytest

RUN pytest