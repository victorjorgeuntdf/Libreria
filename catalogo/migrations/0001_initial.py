# Generated by Django 4.2 on 2025-05-15 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('autor', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('anio_publicacion', models.IntegerField()),
                ('isbn', models.CharField(max_length=13, unique=True)),
            ],
        ),
    ]
