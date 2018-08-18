# Generated by Django 2.0.8 on 2018-08-14 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaTema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'área/tema',
                'verbose_name_plural': 'áreas/temas',
            },
        ),
        migrations.CreateModel(
            name='Avaliador_AreaTema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='trabalhos.AreaTema')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300, verbose_name='título')),
                ('arquivo', models.FileField(upload_to='trabalhos')),
                ('situacao', models.IntegerField(choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Reprovado')], verbose_name='situação', default=0, editable=False)),
                ('area_tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabalhos.AreaTema', verbose_name='área/tema')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('coautor1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('coautor2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('coautor3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modalidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trabalhos.Modalidade')),
            ],
        ),
        migrations.AddField(
            model_name='areatema',
            name='avaliadores',
            field=models.ManyToManyField(through='trabalhos.Avaliador_AreaTema', to=settings.AUTH_USER_MODEL),
        ),
    ]
