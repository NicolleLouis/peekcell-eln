from django.contrib import admin
from django.db import models

class Vial(models.Model):
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
        return f"Vial: {self.sample} - {self.volume} mL - {self.id}"

@admin.register(Vial)
class SampleAdmin(admin.ModelAdmin):
    list_display = (
        'sample',
        'storage',
    )
    search_fields = (
        'id',
    )
    list_filter = [
        'sample',
        'storage',
    ]
    ordering = ('id',)
