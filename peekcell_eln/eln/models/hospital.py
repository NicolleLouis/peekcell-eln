from django.contrib import admin
from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=30)
    clinical_studies = models.ManyToManyField('ClinicalStudy')

    def __str__(self):
        return self.name


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
