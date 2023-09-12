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


class Revenue(BaseModel):
    reference_number = models.CharField(
        max_length=255, help_text='Order ID will be reference number for accounting department'
    )
    revenue_amount = models.DecimalField(max_digits=10, decimal_places=2)
