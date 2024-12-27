from django.db import models
from django.contrib import admin

from eln.models.experiment.experiment import Experiment


class ExperimentFilter(Experiment):
    filter_size = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Filter: {self.vial} - {self.created_at}"

@admin.register(ExperimentFilter)
class ExperimentFilterAdmin(admin.ModelAdmin):
    list_display = (
        'vial',
        'filter_size',
        'created_at',
        'id',
    )
    search_fields = (
        'vial',
        'id',
    )
    ordering = ('created_at',)
