import json
import os
from pathlib import Path

import django
import pika
from dotenv import load_dotenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "warehouse.settings")
django.setup()

env_path = Path('warehouse') / '.env'
load_dotenv(dotenv_path=env_path)

credentials = pika.PlainCredentials(os.environ.get('RABBIT_MQ_USER'), os.environ.get('RABBIT_MQ_PASS'))
params = pika.ConnectionParameters(
    os.environ.get('RABBIT_MQ_HOST'), 5672, os.environ.get('RABBIT_MQ_USER'), credentials, heartbeat=0
)
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='sales', body=json.dumps(body), properties=properties)
