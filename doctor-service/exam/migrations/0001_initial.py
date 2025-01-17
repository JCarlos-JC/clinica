# Generated by Django 5.0.7 on 2024-10-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nid', models.CharField(help_text='Patient NID', max_length=20)),
                ('patient_name', models.CharField(max_length=100)),
                ('exam', models.CharField(choices=[('hemograma', 'Hemograma'), ('glicose', 'Glicose'), ('colesterol_total', 'Colesterol Total'), ('triglicerídeos', 'Triglicerídeos'), ('função_hepatica', 'Função Hepática'), ('função_renal', 'Função Renal'), ('urina_geral', 'Urina Geral'), ('exame_sanguineo', 'Exame Sanguíneo'), ('raio_x', 'Raio X'), ('ultrassom', 'Ultrassom'), ('tomografia_computadorizada', 'Tomografia Computadorizada'), ('ressonancia_magnetica', 'Ressonância Magnética'), ('ecocardiograma', 'Ecocardiograma'), ('teste_de_esforço', 'Teste de Esforço'), ('exame_de_visao', 'Exame de Visão'), ('exame_de_auditivo', 'Exame Auditivo'), ('cultura_de_bactéria', 'Cultura de Bactéria'), ('teste_rápido', 'Teste Rápido'), ('bioquimica', 'Bioquímica'), ('imunologia', 'Imunologia'), ('alergia', 'Alergia')], max_length=50)),
            ],
        ),
    ]
