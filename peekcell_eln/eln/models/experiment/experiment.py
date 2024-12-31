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
    )

    def __str__(self):
        return f"Experiment: {self.created_at.strftime("%Y-%m-%d")}"

@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = (
        'get_experience_type',
        'created_at',
        'id',
    )
    search_fields = (
        'id',
    )
    ordering = ('created_at',)
    filter_horizontal = ('vial',)

    @admin.display(description="Experiment Type")
    def get_experience_type(self, obj):
        if hasattr(obj, 'experimentfilter'):
            return "Filter"
        return "Unknown"
