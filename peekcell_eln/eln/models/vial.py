from django.contrib import admin
from django.db import models


class Vial(models.Model):
    label = models.CharField(
        max_length=255,
        null=True,
        unique=True,
    )
    sample = models.ForeignKey(
        'Sample',
        related_name='vials',
        on_delete=models.PROTECT,
        null=True,
    )
    storage = models.ForeignKey(
        'Storage',
        on_delete=models.PROTECT,
        null=True,
    )
    volume = models.IntegerField(default=0)
    is_closed = models.BooleanField(default=False)
    is_sediment = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def close(self):
        self.is_closed = True
        self.save()

    def __str__(self):
        return f"Vial: {self.label}"

@admin.register(Vial)
class SampleAdmin(admin.ModelAdmin):
    readonly_fields = ('experiments_list',)
    list_display = (
        'label',
        'sample',
        'volume',
        'storage',
    )
    search_fields = (
        'label',
        'id',
    )
    list_filter = [
        'sample',
        'storage',
        'volume',
        'created_at',
    ]
    ordering = ('id',)

    @admin.display(description="Experiments list")
    def experiments_list(self, obj):
        return ", ".join([str(experiment) for experiment in obj.experiments.all()])
