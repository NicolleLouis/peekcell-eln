from django.db import models


class SampleType(models.TextChoices):
    """
    Sample type choices
    """
    BLOOD = 'blood', 'Blood'
    URINE = 'urine', 'Urine'
