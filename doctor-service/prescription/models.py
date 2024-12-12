from django.db import models
from django.utils import timezone

# Parameterized choices for medications based on the MISAU database
MEDICATIONS = [
    ('paracetamol', 'Paracetamol'),
    ('ibuprofeno', 'Ibuprofeno'),
    ('amoxicilina', 'Amoxicilina'),
    ('azitromicina', 'Azitromicina'),
    ('metformina', 'Metformina'),
    ('losartana', 'Losartana'),
    ('anlodipino', 'Anlodipino'),
    ('atorvastatina', 'Atorvastatina'),
    ('salbutamol', 'Salbutamol'),
    ('hidroclorotiazida', 'Hidroclorotiazida'),
    ('enalapril', 'Enalapril'),
    ('omeprazol', 'Omeprazol'),
    ('captopril', 'Captopril'),
    ('clopidogrel', 'Clopidogrel'),
    ('ceftriaxona', 'Ceftriaxona'),
    ('insulina', 'Insulina'),
    ('ácido acetilsalicílico', 'Ácido Acetilsalicílico (AAS)'),
    ('diclofenaco', 'Diclofenaco'),
    ('gentamicina', 'Gentamicina'),
    ('furosemida', 'Furosemida'),
    ('doxiciclina', 'Doxiciclina'),
    ('ciprofloxacina', 'Ciprofloxacina'),
    ('levotiroxina', 'Levotiroxina'),
    ('nifedipina', 'Nifedipina'),
    ('prednisolona', 'Prednisolona'),
    ('varfarina', 'Varfarina'),
    ('sinvastatina', 'Sinvastatina'),
    ('diazepam', 'Diazepam'),
    ('albuterol', 'Albuterol'),
    ('cetoconazol', 'Cetoconazol'),
    ('fluconazol', 'Fluconazol'),
    ('amitriptilina', 'Amitriptilina'),
    ('fenobarbital', 'Fenobarbital'),
    ('quinino', 'Quinino'),
    ('hidroxicloroquina', 'Hidroxicloroquina'),
    ('cloroquina', 'Cloroquina'),
    ('metildopa', 'Metildopa'),
    ('risperidona', 'Risperidona'),
    ('haloperidol', 'Haloperidol'),
    ('cotrimoxazol', 'Cotrimoxazol'),
    ('nevirapina', 'Nevirapina'),
    ('efavirenz', 'Efavirenz'),
    ('zidovudina', 'Zidovudina'),
    ('lamivudina', 'Lamivudina'),
    ('ritonavir', 'Ritonavir'),
    ('abacavir', 'Abacavir'),
    ('dolutegravir', 'Dolutegravir'),
    ('isoniazida', 'Isoniazida'),
    ('etambutol', 'Etambutol'),
    ('rifampicina', 'Rifampicina'),
    ('pirazinamida', 'Pirazinamida'),
    ('mebendazol', 'Mebendazol'),
    ('albendazol', 'Albendazol'),
    ('praziquantel', 'Praziquantel'),
    ('espironolactona', 'Espironolactona'),
    ('glibenclamida', 'Glibenclamida'),
    ('arteméter', 'Arteméter'),
    ('lumefantrina', 'Lumefantrina'),
    ('pirimetamina', 'Pirimetamina'),
    ('sulfadoxina', 'Sulfadoxina'),
    ('bupivacaína', 'Bupivacaína'),
    ('lidocaína', 'Lidocaína'),
    ('morfina', 'Morfina'),
    ('tramadol', 'Tramadol'),
    ('codeína', 'Codeína'),
    ('fentanil', 'Fentanil'),
    ('midazolam', 'Midazolam'),
    ('ondansetrona', 'Ondansetrona'),
    ('metronidazol', 'Metronidazol'),
    ('piperacilina', 'Piperacilina'),
    ('tazobactam', 'Tazobactam'),
    ('clindamicina', 'Clindamicina'),
    ('vancomicina', 'Vancomicina'),
    ('violeta genciana', 'Violeta Genciana'),
    ('dexametasona', 'Dexametasona'),
    ('cetamina', 'Cetamina'),
    ('gluconato de cálcio', 'Gluconato de Cálcio'),
    ('sulfato de magnésio', 'Sulfato de Magnésio'),
    ('fexofenadina', 'Fexofenadina'),
    ('loratadina', 'Loratadina'),
    ('cetirizina', 'Cetirizina'),
    ('digoxina', 'Digoxina'),
    ('bisoprolol', 'Bisoprolol'),
    ('atenolol', 'Atenolol'),
    ('verapamil', 'Verapamil'),
    ('metilprednisolona', 'Metilprednisolona'),
    ('espiramicina', 'Espiramicina'),
    ('glicose', 'Glicose'),
    ('solução eletrolítica', 'Solução Eletrolítica'),
    ('albumina', 'Albumina'),
    ('adrenalina', 'Adrenalina'),
    ('noradrenalina', 'Noradrenalina'),
    ('dopamina', 'Dopamina'),
    ('teofilina', 'Teofilina'),
    ('ipratropio', 'Ipratrópio'),
    ('montelucaste', 'Montelucaste'),
    ('sertralina', 'Sertralina'),
    ('fluoxetina', 'Fluoxetina'),
    ('citalopram', 'Citalopram'),
    ('carbamazepina', 'Carbamazepina'),
    ('ácido valpróico', 'Ácido Valpróico'),
    ('levetiracetam', 'Levetiracetam'),
    ('bicarbonato de sódio', 'Bicarbonato de Sódio'),
]


# Parameterized choices for units
UNIT_CHOICES = [
    ('ml', 'Milliliters (ml)'),
    ('g', 'Grams (g)'),
    ('mg', 'Milligrams (mg)'),
    ('tablets', 'Tablets'),
    # Add more units as needed
]

# Parameterized choices for administration route
ADMIN_ROUTE_CHOICES = [
    ('oral', 'Oral'),
    ('intravenosa', 'Intravenosa'),
    ('intramuscular', 'Intramuscular'),
    ('subcutanea', 'Subcutânea'),
    ('topica', 'Tópica'),
    ('inhalatoria', 'Inalatória'),
    ('sublingual', 'Sublingual'),
    ('retal', 'Retal'),
    ('transdermica', 'Transdérmica'),
    ('oftalmica', 'Oftálmica'),
    ('otica', 'Ótica'),
    ('nasal', 'Nasal'),
    ('vaginal', 'Vaginal'),
    ('intranasal', 'Intranasal'),
    ('intradermica', 'Intradérmica'),
    ('intra-articular', 'Intra-articular'),
    ('intratecal', 'Intratecal'),
    ('intraperitoneal', 'Intraperitoneal'),
]

# Parameterized choices for daily dose
DAILY_DOSE_CHOICES = [
# Parameterized choices for daily doses (in Portuguese)
    ('uma_vez', 'Uma vez ao dia'),
    ('duas_vezes', 'Duas vezes ao dia'),
    ('tres_vezes', 'Três vezes ao dia'),
    ('quatro_vezes', 'Quatro vezes ao dia'),
    ('a_cada_6_horas', 'A cada 6 horas'),
    ('a_cada_8_horas', 'A cada 8 horas'),
    ('a_cada_12_horas', 'A cada 12 horas'),
    ('a_cada_24_horas', 'A cada 24 horas'),
]



class Prescription(models.Model):
    def generate_nid():
            # Obtém o ano atual
            current_year = timezone.now().year
            # Conta o número de pacientes registrados neste ano
            count = Prescription.objects.filter(nid__contains=f'/{current_year}').count() + 1
            # Formata o nid com o número sequencial e o ano
            return f'{str(count).zfill(4)}/{current_year}'
        
    
    nid = models.CharField(max_length=9, unique=True, default=generate_nid, editable=False)
    patient_name = models.CharField(max_length=100, help_text="Name of the Patient")
    medication = models.CharField(
        max_length=50,
        choices=MEDICATIONS,
        blank=True,
        help_text="Select medication from MISAU official database"
    )
    medication_text = models.CharField(
        max_length=100,
        blank=True,
        help_text="Enter medication if not listed in MISAU database"
    )
    quantity = models.DecimalField(max_digits=5, decimal_places=2, help_text="Amount of medication prescribed")
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, help_text="Unit of measurement (e.g., ml, g, mg)")
    administration_route = models.CharField(max_length=20, choices=ADMIN_ROUTE_CHOICES, help_text="Route of administration")
    daily_dose = models.CharField(max_length=20, choices=DAILY_DOSE_CHOICES, help_text="How many times per day the medication should be taken")
    number_of_days = models.PositiveIntegerField(help_text="Number of days the medication should be taken")
    comment = models.TextField(blank=True, help_text="Additional instructions or comments")

    def __str__(self):
        return f"Prescription for {self.patient_name} - {self.medication or self.medication_text}"
