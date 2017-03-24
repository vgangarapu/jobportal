# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=45, null=True)),
                ('last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('gender', models.TextField(blank=True, null=True)),
                ('is_experienced', models.TextField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('resume', models.TextField(blank=True, null=True)),
                ('age', models.DateField(blank=True, null=True)),
                ('current_ctc', models.FloatField(blank=True, null=True)),
                ('phone', models.TextField(blank=True, max_length=15, null=True)),
                ('linkedin', models.CharField(blank=True, db_column='linkedIn', max_length=45, null=True)),
                ('skype', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('years_of_experience', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'candidate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CandidateEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_id', models.IntegerField(blank=True, null=True)),
                ('degree_name', models.CharField(blank=True, max_length=45, null=True)),
                ('year_gradudated', models.DateField(blank=True, null=True)),
                ('university', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'candidate_education',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CandidateExprience',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('is_currently_working', models.TextField(blank=True, null=True)),
                ('company_name', models.CharField(blank=True, max_length=45, null=True)),
                ('company_adress', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=45, null=True)),
                ('city', models.CharField(blank=True, max_length=45, null=True)),
                ('state', models.CharField(blank=True, max_length=45, null=True)),
                ('job_type_id', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'candidate_exprience',
                'managed': False,
            },
        ),
    ]
