from django.contrib import admin
from django.db import models


class ClinicalStudy(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


@admin.register(ClinicalStudy)
class ClinicalStudyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
