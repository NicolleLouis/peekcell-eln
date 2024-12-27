from django.db import models
from django.contrib import admin

class Experiment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    vial = models.ForeignKey(
        'Vial',
        related_name='experiments',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"Experiment: {self.vial} - {self.created_at}"

@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = (
        'vial',
        'get_experience_type',
        'created_at',
        'id',
    )
    search_fields = (
        'vial',
        'id',
    )
    ordering = ('created_at',)

    @admin.display(description="Experiment Type")
    def get_experience_type(self, obj):
        if hasattr(obj, 'experimentfilter'):
            return "Filter"
        return "Unknown"
