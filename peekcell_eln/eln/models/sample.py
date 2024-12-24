from django.contrib import admin
from django.db import models

from eln.models.choices.sample_type import SampleType


class Sample(models.Model):
    person = models.ForeignKey(
        'Person',
        related_name='samples',
        on_delete=models.PROTECT,
        null=True,
    )
    type = models.CharField(
        max_length=5,
        choices=SampleType,
        default=SampleType.URINE,
    )
    storage = models.ForeignKey(
        'Storage',
        on_delete=models.PROTECT,
        null=True,
    )

    def __str__(self):
        return f"Sample: {self.person} - {self.type} - {self.id}"

@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = (
        'person',
        'storage',
        'id',
    )
    search_fields = (
        'id',
    )
    list_filter = [
        'person',
        'storage',
    ]
    ordering = ('id',)
