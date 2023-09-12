import logging
import os

import httpx
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Logging configration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Retrieve environment variables for service URLs
warehouse_service_url = os.environ.get('WAREHOUSE_URL', '')
sales_service_url = os.environ.get('SALES_URL', '')
accounting_service_url = os.environ.get('ACCOUNTING_URL', '')


class PlaceOrderRequest(BaseModel):
    name: str
    email: str
    phone_number: str
    address: str
    city: str
    zip_code: str
    order_quantity: int


@app.post('/api/products/{id}/place-order')
async def place_order(product_id: int, request_body: PlaceOrderRequest):
    warehouse_url = f'{warehouse_service_url}/api/v1/warehouse/products/{product_id}/place-order/'
    response = await make_request(warehouse_url, 'POST', request_body.dict())
    if response is None:
        return {'error': 'Failed to place order'}

    return {'data': response}


async def make_request(url, method, params=None, headers=None):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.request(method, url, headers=headers, json=params)
            return response.json()
    except httpx.HTTPError as e:
        logger.error(f'HTTP Error occurred while fetching data: {e}')
    except Exception as e:
        logger.error(f'An error occurred while fetching data: {e}')
    return None


@app.get('/api/order-details/{id}')
async def order_details(order_id: int):
    sales_url = f'{sales_service_url}/api/v1/sales/order-details/{order_id}/'
    response = await make_request(sales_url, 'GET')
    if response is None:
        return {'error': 'Failed to fetch order details'}

    return {'data': response}


@app.get('/api/revenue-details/')
async def revenue_details():
    accounting_url = f'{accounting_service_url}/api/v1/accounting/revenue-details/'
    response = await make_request(accounting_url, 'GET')
    if response is None:
        return {'error': 'Failed to fetch revenue details'}

    return {'data': response}


@app.get('/api/products')
async def products():
    warehouse_url = f'{warehouse_service_url}/api/v1/warehouse/products/'
    response = await make_request(warehouse_url, 'GET')
    if response is None:
        return {'error': 'Failed to fetch products details'}

    return {'data': response}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
