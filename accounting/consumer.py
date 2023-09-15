import json
import logging
import os
from pathlib import Path

import django
import pika
from django.db import transaction
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path('accounting') / '.env')
django.setup()

from core.models import Revenue

logger = logging.getLogger(__name__)

credentials = pika.PlainCredentials(os.environ.get('RABBIT_MQ_USER'), os.environ.get('RABBIT_MQ_PASS'))
params = pika.ConnectionParameters(
    os.environ.get('RABBIT_MQ_HOST'), 5672, os.environ.get('RABBIT_MQ_USER'), credentials, heartbeat=0
)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='accounting')


def callback(ch, method, properties, body):
    logger.info('Received in warehouse')
    data = json.loads(body)
    logger.info(f'Received data: {data}')
    with transaction.atomic():
        Revenue.objects.create(order_number=data.get('order_id'), revenue_amount=data.get('order_amount'))
        logger.info('Revenue is added.')


channel.basic_consume(queue='accounting', on_message_callback=callback, auto_ack=True)
try:
    logger.info('Started Consuming')
    channel.start_consuming()
except KeyboardInterrupt:
    logger.info('Consuming stopped by user.')
finally:
    channel.close()
    connection.close()
