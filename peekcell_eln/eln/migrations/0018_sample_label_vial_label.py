# Generated by Django 5.1.4 on 2024-12-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eln', '0017_remove_experiment_vial_experiment_vial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='label',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vial',
            name='label',
            field=models.CharField(max_length=255, null=True),
        ),
    ]