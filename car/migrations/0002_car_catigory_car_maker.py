# Generated by Django 5.0.6 on 2024-06-30 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='catigory',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='car.catigory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='maker',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='car.maker'),
            preserve_default=False,
        ),
    ]
