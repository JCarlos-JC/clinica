# Generated by Django 5.0.7 on 2024-12-01 21:02

import exam.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='nid',
            field=models.CharField(default=exam.models.generate_nid, editable=False, max_length=9, unique=True),
        ),
    ]
