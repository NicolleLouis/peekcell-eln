from django.db import models
from django.contrib import admin

from eln.models import Consumable
from eln.models.admin.product_admin import open_products, close_products
from eln.models.choices.product_name import ProductName


class Product(Consumable):
    name = models.CharField(
        max_length=34,
        choices=ProductName.choices,
        default=ProductName.CHLOROFORM
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'status',
    )
    search_fields = (
        'name',
    )
    list_filter = [
        'name',
        'status',
    ]
    ordering = ('id',)
    actions = [open_products, close_products]
