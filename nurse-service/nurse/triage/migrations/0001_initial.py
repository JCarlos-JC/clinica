# Generated by Django 5.0.7 on 2024-12-03 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=255)),
                ('height', models.FloatField(help_text='Height of the patient in meters (m)')),
                ('weight', models.FloatField(help_text='Weight of the patient in kilograms (kg)')),
                ('blood_pressure', models.CharField(help_text='Blood pressure of the patient in millimeters of mercury (mmHg)', max_length=20)),
                ('heart_rate', models.IntegerField(help_text='Heart rate of the patient in beats per minute (bpm)')),
                ('temperature', models.FloatField(help_text='Temperature of the patient in degrees Celsius (°C)')),
                ('oximetry', models.FloatField(help_text='Blood oxygen saturation level of the patient in percentage (%)')),
                ('capillary_glucose', models.FloatField(help_text='Capillary blood glucose of the patient in milligrams per deciliter (mg/dL)')),
            ],
        ),
    ]
