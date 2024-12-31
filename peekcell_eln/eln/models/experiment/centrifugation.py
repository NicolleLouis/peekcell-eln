from django.db import models
from django.contrib import admin

from eln.models.experiment.experiment import Experiment


class ExperimentCentrifugation(Experiment):
    speed = models.IntegerField(
        help_text="G",
        default=2000,
    )
    duration = models.IntegerField(
        help_text="Minutes",
        default=10,
    )
    temperature = models.IntegerField(
        help_text="Degrees Celsius",
        default=4,
    )

    def __str__(self):
        return f"Centrifugation: {self.created_at}"

@admin.register(ExperimentCentrifugation)
class ExperimentCentrifugationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'speed',
        'duration',
        'temperature',
        'created_at',
    )
    search_fields = (
        'id',
    )
    ordering = ('created_at',)
