from django.db import models
from django.contrib import admin

from eln.models.experiment.experiment import Experiment


class ExperimentFilter(Experiment):
    filter_size = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Filter: {self.created_at}"

@admin.register(ExperimentFilter)
class ExperimentFilterAdmin(admin.ModelAdmin):
    list_display = (
        'filter_size',
        'created_at',
        'id',
    )
    search_fields = (
        'id',
    )
    ordering = ('created_at',)
