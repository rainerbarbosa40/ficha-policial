# Generated by Django 5.1.1 on 2024-09-14 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FichaPolicial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('grad', models.TextField(blank=True, null=True)),
                ('matr', models.IntegerField(blank=True, null=True, unique=True)),
                ('nome', models.TextField(blank=True, null=True)),
                ('ome', models.TextField(blank=True, null=True)),
                ('dispo', models.TextField(blank=True, null=True)),
                ('sexo', models.TextField(blank=True, null=True)),
                ('cpf', models.TextField(blank=True, null=True)),
                ('quadro', models.TextField(blank=True, null=True)),
                ('rg', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ficha_policial',
            },
        ),
    ]
