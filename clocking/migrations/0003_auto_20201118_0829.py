# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-11-18 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clocking', '0002_auto_20201117_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roster',
            name='roster_shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roster_shift', to='clocking.Shift'),
        ),
    ]
