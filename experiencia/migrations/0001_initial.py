# Generated by Django 3.2.4 on 2022-01-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='experiencia')),
                ('empresa', models.CharField(max_length=50)),
                ('periodo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('habilidadesCom', models.CharField(max_length=50)),
                ('td', models.JSONField()),
                ('habilidAdq', models.CharField(max_length=50)),
                ('li', models.JSONField()),
            ],
        ),
    ]
