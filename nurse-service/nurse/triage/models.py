from django.db import models

class Screening(models.Model):  # 'Triagem' -> 'Screening'
    patient_name = models.CharField(max_length=255)  # 'nome_patient' -> 'patient_name'
    height = models.FloatField(help_text="Height of the patient in meters (m)")  # 'altura' -> 'height'
    weight = models.FloatField(help_text="Weight of the patient in kilograms (kg)")  # 'peso' -> 'weight'
    blood_pressure = models.CharField(max_length=20, help_text="Blood pressure of the patient in millimeters of mercury (mmHg)")  # 'pressao_arterial' -> 'blood_pressure'
    heart_rate = models.IntegerField(help_text="Heart rate of the patient in beats per minute (bpm)")  # 'frequencia_cardiaca' -> 'heart_rate'
    temperature = models.FloatField(help_text="Temperature of the patient in degrees Celsius (°C)")  # 'temperatura' -> 'temperature'
    oximetry = models.FloatField(help_text="Blood oxygen saturation level of the patient in percentage (%)")  # 'oximetria' -> 'oximetry'
    capillary_glucose = models.FloatField(help_text="Capillary blood glucose of the patient in milligrams per deciliter (mg/dL)")  # 'glicemia_capilar' -> 'capillary_glucose'

def __str__(self):
    return f"Screening for patient {self.patient_name}"
