# nurses/models.py
from django.db import models

class Nurse(models.Model):
    GENERO = (
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
    )

    nome = models.CharField(max_length=255)
    genero = models.CharField(
        max_length=20,
        choices=GENERO,
    )
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, blank=True)
    data_nascimento = models.DateField()
    data_contratacao = models.DateTimeField()
    especialidade = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"
