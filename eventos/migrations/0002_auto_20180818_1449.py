# Generated by Django 2.0.8 on 2018-08-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atividade',
            old_name='modalidade',
            new_name='tipo',
        ),
        migrations.AddField(
            model_name='inscricao',
            name='atividades',
            field=models.ManyToManyField(related_name='inscricoes', to='eventos.Atividade'),
        ),
    ]
