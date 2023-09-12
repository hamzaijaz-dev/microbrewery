from django.db import models


class BaseModel(models.Model):
    """
    Provide default fields that are expectedly to be needed by almost all
    models
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Customer(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Order(BaseModel):
    PENDING = 1
    CONFIRMED = 2
    IN_TRANSIT = 3
    DELIVERED = 4
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (IN_TRANSIT, 'In-Transit'),
        (DELIVERED, 'Delivered'),
    )

    COD = 1
    CARD = 2
    PAYMENT_TYPE_CHOICES = (
        (COD, 'Cash On Delivery'),
        (CARD, 'Card'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order')
    payment_type = models.PositiveSmallIntegerField(choices=PAYMENT_TYPE_CHOICES, default=COD)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=PENDING)
    product_sku = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
