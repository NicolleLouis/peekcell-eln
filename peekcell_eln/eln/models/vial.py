from django.contrib import admin
from django.db import models

class Vial(models.Model):
    sample = models.ForeignKey(
        'Sample',
        on_delete=models.PROTECT,
        null=True,
    )
    volume = models.IntegerField(default=0)

    def __str__(self):
        return f"Vial: {self.sample} - {self.volume} mL - {self.id}"

@admin.register(Vial)
class SampleAdmin(admin.ModelAdmin):
    list_display = (
        'sample',
        'volume',
    )
    search_fields = (
        'id',
    )
    list_filter = [
        'sample',
    ]
    ordering = ('id',)