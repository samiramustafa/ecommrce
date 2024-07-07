# Generated by Django 5.0.6 on 2024-07-02 20:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_alter_car_catigory_alter_car_maker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='catigory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.catigory'),
        ),
        migrations.AlterField(
            model_name='car',
            name='maker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.maker'),
        ),
    ]