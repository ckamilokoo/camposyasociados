# Generated by Django 4.1.7 on 2023-03-20 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='')),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
