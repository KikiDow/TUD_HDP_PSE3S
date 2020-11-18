# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-11-18 18:47
from __future__ import unicode_literals

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
            name='CertifiedSickLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_day_of_cert', models.DateField()),
                ('last_day_of_cert', models.DateField()),
                ('csl_image', models.ImageField(upload_to='csl_images')),
                ('date_csl_submitted', models.DateTimeField(auto_now_add=True)),
                ('csl_checked_by_validator', models.BooleanField(default=False)),
                ('csl_accepted', models.BooleanField(default=False)),
                ('reason_csl_rejected', models.CharField(blank=True, max_length=400, null=True)),
                ('csl_officer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='csl_officer_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CertifiedSickPerYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csl_year', models.IntegerField()),
                ('number_csl_for_year', models.IntegerField()),
                ('yearly_csl_officer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yearly_csl_officer_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ForceMajeure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fm_date', models.DateField()),
                ('reason_for_fm', models.CharField(max_length=600)),
                ('date_fm_submitted', models.DateTimeField(auto_now_add=True)),
                ('fm_checked_by_validator', models.BooleanField(default=False)),
                ('fm_accepted', models.BooleanField(default=False)),
                ('reason_fm_rejected', models.CharField(blank=True, max_length=600, null=True)),
                ('fm_officer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fm_officer_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ForceMajeurePerYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fm_year', models.IntegerField()),
                ('number_fm_for_year', models.IntegerField()),
                ('yearly_fm_officer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yearly_fm_officer_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UnCertifiedSickLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usl_date', models.DateField()),
                ('reason_for_usl', models.CharField(max_length=600)),
                ('date_usl_submitted', models.DateTimeField(auto_now_add=True)),
                ('usl_checked_by_validator', models.BooleanField(default=False)),
                ('usl_accepted', models.BooleanField(default=False)),
                ('reason_usl_rejected', models.CharField(blank=True, max_length=600, null=True)),
                ('usl_officer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usl_officer_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UnCertifiedSickPerYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usl_year', models.IntegerField()),
                ('number_usl_for_year', models.IntegerField()),
                ('yearly_usl_officer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yearly_usl_officer_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
