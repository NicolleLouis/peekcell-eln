from django.contrib import admin
from django.db import models


class Storage(models.Model):
    label = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.label}"


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = (
        'label',
        'id',
    )
    search_fields = (
        'label',
    )
    list_filter = [
        'label',
    ]
    ordering = ('label',)
