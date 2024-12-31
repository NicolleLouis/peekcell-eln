from django.db import models


class RNAExtractionProductName(models.TextChoices):
    """
    Product
    """
    URINE_MICRORNA_KIT = 'urine_microrna_kit', 'Urine miRNA Kit'
    MIRNEASY_ADVANCED_MINI_KIT = 'mirneasy_advanced_mini_kit', 'miRNeasy Advanced Mini Kit'
    MIRNEASY_SERUM_PLASMA_ADVANCED_KIT = 'mirneasy_serum_plasma_advanced_kit', 'miRNeasy Serum/Plasma Advanced Kit'
