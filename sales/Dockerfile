FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /sales
COPY /requirements.txt /sales/requirements.txt
RUN pip install -r requirements.txt
COPY . /sales
