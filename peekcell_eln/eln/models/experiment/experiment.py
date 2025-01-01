from django.db import models
from django.contrib import admin

class Experiment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    vial = models.ManyToManyField(
        'Vial',
        related_name='experiments',
    )
    comment = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Experiment: {self.created_at.strftime("%Y-%m-%d")}"

    @property
    def experience_type(self):
        if hasattr(self, 'experimentfilter'):
            return "Filter"
        if hasattr(self, 'experimentcentrifugation'):
            return "Centrifugation"
        if hasattr(self, 'experimentrnaextraction'):
            return "RNA Extraction"
        if hasattr(self, 'experimentreversetranscriptase'):
            return "Reverse Transcriptase"
        if hasattr(self, 'experimentqpcr'):
            return "qPCR"
        return "Unknown"

@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'experience_type',
        'created_at',
    )
    search_fields = (
        'id',
    )
    ordering = ('created_at',)
    filter_horizontal = ('vial',)
