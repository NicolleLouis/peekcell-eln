from django.db import models
from django.contrib import admin

from eln.models.choices.rna_extraction_product import RNAExtractionProductName
from eln.models.experiment.experiment import Experiment


class ExperimentRNAExtraction(Experiment):
    kit = models.CharField(
        choices=RNAExtractionProductName.choices,
        max_length=34,
        null=False,
        default=RNAExtractionProductName.MIRNEASY_SERUM_PLASMA_ADVANCED_KIT,
    )
    input_volume = models.IntegerField(
        help_text="µL",
        default=500,
    )
    elution_volume = models.IntegerField(
        help_text="µL",
        default=10,
    )
    contain_spike_in = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"RNAExtraction: {self.created_at}"

@admin.register(ExperimentRNAExtraction)
class ExperimentRNAExtractionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'kit',
        'input_volume',
        'elution_volume',
        'contain_spike_in',
        'created_at',
    )
    search_fields = (
        'id',
    )
    list_filter = [
        'contain_spike_in',
        'kit',
    ]
    ordering = ('created_at',)
