FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip3 install  -r requirements.txt
COPY . /code/

