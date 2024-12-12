from django.db import models

class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=50)
    crm = models.CharField(max_length=15, unique=True)
    contact = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=200, blank=True)
    neighborhood = models.CharField(max_length=60, blank=True)
    block = models.CharField(max_length=15, blank=True)
    house_number = models.CharField(max_length=15, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
