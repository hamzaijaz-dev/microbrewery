FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /warehouse
COPY /requirements.txt /warehouse/requirements.txt
RUN pip install -r requirements.txt
COPY . /warehouse
