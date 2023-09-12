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


class Warehouse(BaseModel):
    name = models.CharField(max_length=100)
    location = models.TextField()

    def __str__(self):
        return self.name

    @property
    def total_products(self):
        return self.total_products.count()


class Product(BaseModel):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    initial_stock = models.PositiveIntegerField(default=0)
    remaining_quantity = models.PositiveIntegerField(default=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
