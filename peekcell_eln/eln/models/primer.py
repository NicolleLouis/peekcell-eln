from django.db import models
from django.contrib import admin

from eln.models.admin.product_admin import open_products, close_products
from eln.models.consumable import Consumable


class Primer(Consumable):
    name = models.CharField(
        max_length=32,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


@admin.register(Primer)
class PrimerAdmin(admin.ModelAdmin):
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
