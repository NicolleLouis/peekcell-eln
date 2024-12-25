from django.db import models


class ProductType(models.TextChoices):
    """
    Product Type
    """
    KIT = 'kit', 'Kit'
    PRIMER = 'primer', 'Primer'
