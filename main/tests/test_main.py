from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_place_order():
    order_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "phone_number": "123-456-7890",
        "address": "123 Main St",
        "city": "Sample City",
        "zip_code": "12345",
        "order_quantity": 3
    }
    response = client.post('/api/products/1/place-order', json=order_data)
    assert response.status_code == 200
    assert 'data' in response.json()


def test_place_order_invalid_product_id():
    order_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "phone_number": "123-456-7890",
        "address": "123 Main St",
        "city": "Sample City",
        "zip_code": "12345",
        "order_quantity": 3
    }
    response = client.post('/api/products/999/place-order', json=order_data)
    assert response.status_code == 404
    assert 'error' in response.json()


def test_fetch_products():
    response = client.get('/api/products')
    assert response.status_code == 200
    assert 'data' in response.json()


def test_fetch_products_invalid_url():
    app.warehouse_service_url = 'http://invalid-url'
    response = client.get('/api/products')
    assert response.status_code == 500
    assert 'error' in response.json()


def test_place_order_missing_fields():
    order_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "phone_number": "123-456-7890",
        # Missing fields: address, city, zip_code, order_quantity
    }
    response = client.post('/api/products/1/place-order', json=order_data)
    assert response.status_code == 422


def test_place_order_negative_quantity():
    order_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "phone_number": "123-456-7890",
        "address": "123 Main St",
        "city": "Sample City",
        "zip_code": "12345",
        "order_quantity": -3
    }
    response = client.post('/api/products/1/place-order', json=order_data)
    assert response.status_code == 422


def test_place_order_invalid_email():
    order_data = {
        "name": "John Doe",
        "email": "johnexample.com",
        "phone_number": "123-456-7890",
        "address": "123 Main St",
        "city": "Sample City",
        "zip_code": "12345",
        "order_quantity": 3
    }
    response = client.post('/api/products/1/place-order', json=order_data)
    assert response.status_code == 422


def test_fetch_products_timeout_error():
    app.warehouse_service_url = 'http://unreachable-url'
    response = client.get('/api/products')
    assert response.status_code == 500
    assert 'error' in response.json()
