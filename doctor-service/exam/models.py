from django.db import models
from django.utils import timezone

# Create your models here.


EXAM_CHOICES = [
    ('hemograma', 'Hemograma'),
    ('glicose', 'Glicose'),
    ('colesterol_total', 'Colesterol Total'),
    ('triglicerídeos', 'Triglicerídeos'),
    ('função_hepatica', 'Função Hepática'),
    ('função_renal', 'Função Renal'),
    ('urina_geral', 'Urina Geral'),
    ('exame_sanguineo', 'Exame Sanguíneo'),
    ('raio_x', 'Raio X'),
    ('ultrassom', 'Ultrassom'),
    ('tomografia_computadorizada', 'Tomografia Computadorizada'),
    ('ressonancia_magnetica', 'Ressonância Magnética'),
    ('ecocardiograma', 'Ecocardiograma'),
    ('teste_de_esforço', 'Teste de Esforço'),
    ('exame_de_visao', 'Exame de Visão'),
    ('exame_de_auditivo', 'Exame Auditivo'),
    ('cultura_de_bactéria', 'Cultura de Bactéria'),
    ('teste_rápido', 'Teste Rápido'),
    ('bioquimica', 'Bioquímica'),
    ('imunologia', 'Imunologia'),
    ('alergia', 'Alergia'),
]

def generate_nid():
            # Obtém o ano atual
            current_year = timezone.now().year
            # Conta o número de pacientes registrados neste ano
            count = Exam.objects.filter(nid__contains=f'/{current_year}').count() + 1
            # Formata o nid com o número sequencial e o ano
            return f'{str(count).zfill(4)}/{current_year}'

class Exam(models.Model):
    nid = models.CharField(max_length=9, unique=True, default=generate_nid, editable=False)
    patient_name = models.CharField(max_length=100)
    exam = models.CharField(max_length=50, choices=EXAM_CHOICES)

    def __str__(self):
        return f"Exam for {self.patient_name} - {self.get_exam_display()}"

