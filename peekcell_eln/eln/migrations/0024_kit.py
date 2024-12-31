# Generated by Django 5.1.4 on 2024-12-31 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eln', '0023_alter_experimentreversetranscriptase_kit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('kit', 'Kit'), ('primer', 'Primer')], default='kit', max_length=6)),
                ('status', models.CharField(choices=[('received', 'Received'), ('opened', 'Opened'), ('closed', 'Closed')], default='received', max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('opened_at', models.DateTimeField(blank=True, null=True)),
                ('finished_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]