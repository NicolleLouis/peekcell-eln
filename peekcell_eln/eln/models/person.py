from django.contrib import admin
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    hospital = models.ForeignKey(
        'Hospital',
        on_delete=models.PROTECT,
        null=True,
    )
    clinical_study = models.ForeignKey(
        'ClinicalStudy',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    is_test = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'is_test',
        'hospital',
    )
    search_fields = (
        'first_name',
        'last_name',
    )
    list_filter = [
        'hospital',
        'clinical_study',
        'is_test',
    ]
    ordering = ('last_name',)
