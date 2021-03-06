# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-11-21 09:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clocking', '0004_personaldetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_date', models.DateField()),
                ('replacement_date', models.DateField()),
                ('exchange_shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exchange_shift', to='clocking.Shift')),
                ('exchanging_officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exchanging_officer', to=settings.AUTH_USER_MODEL)),
                ('replacement_shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replacement_shift', to='clocking.Shift')),
                ('replacing_officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replacing_officer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_req_date', models.DateField()),
                ('exchange_req_shift_label', models.CharField(max_length=3)),
                ('exchanging_req_officer_notes', models.CharField(blank=True, max_length=600, null=True)),
                ('replacing_req_date', models.DateField(blank=True, null=True)),
                ('replacing_req_shift', models.CharField(blank=True, max_length=3, null=True)),
                ('replacing_req_officer_notes', models.CharField(blank=True, max_length=600, null=True)),
                ('eo_proceed_with_swap', models.BooleanField(default=False)),
                ('ro_proceed_with_swap', models.BooleanField(default=False)),
                ('swap_confirmed', models.BooleanField(default=False)),
                ('swap_cancelled', models.BooleanField(default=False)),
                ('reason_exchange_cancelled', models.CharField(blank=True, max_length=600, null=True)),
                ('exchanging_req_officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exchanging_req_officer', to=settings.AUTH_USER_MODEL)),
                ('replacing_req_officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replacing_req_officer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_started', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('possible_exchange_date', models.DateField(blank=True, null=True)),
                ('post_content', models.CharField(blank=True, max_length=600, null=True)),
                ('likes', models.IntegerField(default=0)),
                ('post_led_to_exchange', models.BooleanField(default=False)),
                ('possible_exchange_shift_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='possible_exchange_shift_id', to='clocking.Shift')),
                ('postee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postee_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='post_liked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_liked', to='exchanges.Post'),
        ),
        migrations.AddField(
            model_name='like',
            name='post_liked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_liked_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
