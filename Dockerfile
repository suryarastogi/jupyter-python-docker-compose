FROM python:3
ENV PYTHONBUFFERED 1

WORKDIR /src

ADD requirements.txt /src/
RUN pip install -r requirements.txt

ADD . /src
RUN pip install .