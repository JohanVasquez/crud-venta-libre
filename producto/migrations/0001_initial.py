# Generated by Django 2.0.6 on 2018-06-11 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=200)),
                ('unidades_ventidas', models.IntegerField()),
                ('fecha_venta', models.DateTimeField(verbose_name='Fecha de venta')),
            ],
        ),
    ]
