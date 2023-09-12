FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /accounting
COPY /requirements.txt /accounting/requirements.txt
RUN pip install -r requirements.txt
COPY . /accounting
