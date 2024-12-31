from django.db import models
from django.contrib import admin

from eln.models.choices.reverse_transcriptase_product import ReverseTranscriptaseProductName
from eln.models.experiment.experiment import Experiment


class ExperimentReverseTranscriptase(Experiment):
    kit = models.CharField(
        choices=ReverseTranscriptaseProductName.choices,
        max_length=18,
        null=False,
        blank=False,
        default=ReverseTranscriptaseProductName.MIRCURY_LNA_RT_KIT,
    )
    rna_dilution = models.BooleanField(
        default=False,
    )
    dilution_rna_volume = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
    )
    dilution_water_volume = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
    )
    input_volume = models.IntegerField(
        help_text="µL",
        default=2,
    )

    def __str__(self):
        return f"ReverseTranscriptase: {self.created_at}"

@admin.register(ExperimentReverseTranscriptase)
class ExperimentReverseTranscriptaseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'kit',
        'rna_dilution',
        'dilution_rna_volume',
        'dilution_water_volume',
        'input_volume',
        'created_at',
    )
    search_fields = (
        'id',
    )
    ordering = ('created_at',)
