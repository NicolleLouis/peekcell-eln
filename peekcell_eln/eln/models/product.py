from django.db import models
from django.utils.timezone import now
from django.contrib import admin

from eln.models.admin.product_admin import open_products, close_products
from eln.models.choices.product_name import ProductName
from eln.models.choices.product_status import ProductStatus
from eln.models.choices.product_type import ProductType


class Product(models.Model):
    name = models.CharField(
        max_length=34,
        choices=ProductName.choices,
        default=ProductName.CHLOROFORM
    )
    type = models.CharField(
        max_length=6,
        choices=ProductType.choices,
        default=ProductType.KIT
    )
    status = models.CharField(
        max_length=8,
        choices=ProductStatus.choices,
        default=ProductStatus.RECEIVED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    opened_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def open(self):
        if self.status == ProductStatus.OPENED:
            return
        if self.status == ProductStatus.CLOSED:
            raise ValueError('Product is already closed')
        self.status = ProductStatus.OPENED
        self.opened_at = now()
        self.save()

    def close(self):
        if self.status == ProductStatus.CLOSED:
            return
        if self.status == ProductStatus.RECEIVED:
            raise ValueError('Product was not opened')
        self.status = ProductStatus.CLOSED
        self.finished_at = now()
        self.save()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'type',
        'status',
    )
    search_fields = (
        'name',
    )
    list_filter = [
        'name',
        'status',
        'type',
    ]
    ordering = ('id',)
    actions = [open_products, close_products]
