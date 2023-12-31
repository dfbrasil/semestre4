# Generated by Django 4.2.7 on 2023-11-16 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade:')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(blank=True, choices=[('Apicultura', 'Apicultura'), ('ADS', 'ADS'), ('Alimentos', 'Alimentos'), ('Quimica', 'Química')], max_length=100, null=True, verbose_name='Curso:')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_aluno', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nome do Aluno')),
                ('email', models.EmailField(blank=True, max_length=250, null=True, verbose_name='Email:')),
                ('idade', models.IntegerField(blank=True, null=True, verbose_name='Idade:')),
                ('endereco', models.CharField(blank=True, max_length=250, null=True, verbose_name='Endereco do Aluno')),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aluno.cidade', verbose_name='Endereço do aluno')),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aluno.curso', verbose_name='Curso')),
            ],
        ),
    ]
