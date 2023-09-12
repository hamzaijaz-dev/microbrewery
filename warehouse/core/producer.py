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

params = pika.URLParameters(os.environ.get('RABBIT_MQ_URL'))
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='sales', body=json.dumps(body), properties=properties)
