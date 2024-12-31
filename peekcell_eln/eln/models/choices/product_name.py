from django.db import models


class ProductName(models.TextChoices):
    """
    Product
    """
    CHLOROFORM = 'chloroform', 'Chloroform'
    TRIZOL = 'trizol', 'Trizol'
    ISOPROPANOL = 'isopropanol', 'Isopropanol'
    BETA_MERCAPTOETHANOL = 'beta_mercaptoethanol', 'Beta-mercaptoethanol'
    URINE_MICRORNA_KIT = 'urine_microrna_kit', 'Urine miRNA Kit'
    MIRNEASY_ADVANCED_MINI_KIT = 'mirneasy_advanced_mini_kit', 'miRNeasy Advanced Mini Kit'
    MIRNEASY_SERUM_PLASMA_ADVANCED_KIT = 'mirneasy_serum_plasma_advanced_kit', 'miRNeasy Serum/Plasma Advanced Kit'
    MIRCURY_LNA_RT_KIT = 'mircury_lna_rt_kit', 'miRCURY LNA RT Kit'
    MIRCURY_LNA_PCR_KIT = 'mircury_lna_pcr_kit', 'miRCURY LNA PCR Kit'
    SPIKE_IN_KIT  = 'spike_in_kit', 'Spike-in Kit'
