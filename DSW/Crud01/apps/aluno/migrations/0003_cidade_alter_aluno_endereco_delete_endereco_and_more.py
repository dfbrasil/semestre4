# Generated by Django 4.2.7 on 2023-11-15 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0002_aluno_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade:')),
            ],
        ),
        migrations.AlterField(
            model_name='aluno',
            name='endereco',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Endereco do Aluno'),
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
        migrations.AddField(
            model_name='aluno',
            name='cidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aluno.cidade', verbose_name='Endereço do aluno'),
        ),
    ]