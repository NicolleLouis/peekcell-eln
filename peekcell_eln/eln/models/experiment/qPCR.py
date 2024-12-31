from django.db import models
from django.contrib import admin

from eln.models.experiment.experiment import Experiment


class ExperimentQPCR(Experiment):
    primer = models.ManyToManyField(
        'Primer',
    )

    def __str__(self):
        return f"QPCR: {self.created_at}"

@admin.register(ExperimentQPCR)
class ExperimentQPCRAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
    )
    search_fields = (
        'id',
    )
    ordering = ('created_at',)
