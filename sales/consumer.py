import json
import logging
import os
from pathlib import Path

import django
import pika
from django.db import transaction
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path('sales') / '.env')
django.setup()

from core.models import Customer, Order

logger = logging.getLogger(__name__)

credentials = pika.PlainCredentials(os.environ.get('RABBIT_MQ_USER'), os.environ.get('RABBIT_MQ_PASS'))
params = pika.ConnectionParameters(
    os.environ.get('RABBIT_MQ_HOST'), 5672, os.environ.get('RABBIT_MQ_USER'), credentials, heartbeat=0
)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='sales')


def callback(ch, method, properties, body):
    logger.info('Received in sales')
    data = json.loads(body)
    if properties.content_type == 'product_available':
        with transaction.atomic():
            customer_data = data.get('request_data')
            customer = {
                'name': customer_data.get('name'),
                'email': customer_data.get('email'),
                'phone_number': customer_data.get('phone_number'),
                'city': customer_data.get('city'),
                'zip_code': customer_data.get('zip_code'),
                'address': customer_data.get('address'),
            }
            customer = Customer.objects.create(**customer)
            order_quantity = data.get('request_data').get('order_quantity')
            price = data.get('price')
            order_amount = order_quantity * price
            logger.info(f'Order amount: {order_amount}')
            order = Order.objects.create(
                product_sku=data.get('product_sku'), customer=customer, order_amount=order_amount
            )
            logger.info('Order is placed successfully.')
            request_body = {'order_amount': order.order_amount, 'order_id': order.id, 'product_sku': order.product_sku}
            channel.basic_publish(exchange='', routing_key='warehouse', body=json.dumps(request_body))
            logger.info('Confirmation is sent to warehouse')


channel.basic_consume(queue='sales', on_message_callback=callback, auto_ack=True)
try:
    logger.info('Started Consuming')
    channel.start_consuming()
except KeyboardInterrupt:
    logger.info('Consuming stopped by user.')
finally:
    channel.close()
    connection.close()
