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


class ExpenseType(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Revenue(BaseModel):
    order_number = models.CharField(max_length=255)
    revenue_amount = models.DecimalField(max_digits=10, decimal_places=2)


class Expense(BaseModel):
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE, related_name='expense_details')
