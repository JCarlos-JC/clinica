from django.db import models
from django.utils import timezone

# Create your models here.


class Patient(models.Model):
    ESTADO = (
        ('grave', 'Grave'),
        ('ligeiro', 'Ligeiro'),
    )
    
    


    TIPO = (
        ('estudante','Estudante'),
        ('bolseiro', 'Bolseiro'),
        ('docente', 'Docente'),
        ('funcionario(cta)', 'Funcionacio(CTA)'),
        ('comunidade', 'comunidade'),
        ('externo', 'Externo')
    )
    GENERO = (
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
    )
    # Método para gerar automaticamente o nid no formato 0000/ano
    def generate_nid():
        # Obtém o ano atual
        current_year = timezone.now().year
        # Conta o número de pacientes registrados neste ano
        count = Patient.objects.filter(nid__contains=f'/{current_year}').count() + 1
        # Formata o nid com o número sequencial e o ano
        return f'{str(count).zfill(4)}/{current_year}'

    nid = models.CharField(max_length=9, unique=True, default=generate_nid, editable=False)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    genero = models.CharField(
        max_length=20,
        choices=GENERO,
    )
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    contacto_de_emergencia = models.CharField(max_length=15, blank=True)
    contacto_familia = models.CharField(max_length=15, blank=True)
    email=models.CharField(max_length=200, blank=True)
    bairro=models.CharField(max_length=60, blank=True)
    quarteirao=models.CharField(max_length=15, blank=True)
    nr_casa=models.CharField(max_length=15, blank=True)
    data_entrada = models.DateTimeField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADO,
    )
    tipo = models.CharField(
        max_length=60,
        choices=TIPO,
        null=True, blank=True,
    )
    nr_estudante = models.CharField (max_length=9, null=True, blank=True)
    nr_funcionario = models.CharField (max_length=9, null=True, blank=True)


    def __str__(self):
        return f"{self.nome} - {self.nid}"


