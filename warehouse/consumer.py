import json
import logging
import os
from pathlib import Path

import django
import pika
from django.db import transaction
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path('warehouse') / '.env')
django.setup()

from core.models import Product

logger = logging.getLogger(__name__)

params = pika.URLParameters(os.environ.get('RABBIT_MQ_URL'))
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='warehouse')


def callback(ch, method, properties, body):
    try:
        logger.info('Received in warehouse')
        data = json.loads(body)
        logger.info(f'Received data: {data}')
        with transaction.atomic():
            product = Product.objects.select_for_update().get(sku=data['product_sku'])
            product.remaining_quantity -= 1
            product.save()

        logger.info(f'One product is sold. SKU: {data["product_sku"]}')
        logger.info('Sending notification to accounting department')
        channel.basic_publish(exchange='', routing_key='accounting', body=json.dumps(data))
        logger.info('Confirmation is sent to accounting')

    except Product.DoesNotExist:
        logger.error(f'Product with SKU {data["product_sku"]} not found in the database.')


channel.basic_consume(queue='warehouse', on_message_callback=callback, auto_ack=True)
try:
    logger.info('Started Consuming')
    channel.start_consuming()
except KeyboardInterrupt:
    logger.info('Consuming stopped by user.')
finally:
    channel.close()
    connection.close()
