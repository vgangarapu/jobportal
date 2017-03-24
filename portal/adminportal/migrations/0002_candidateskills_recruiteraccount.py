# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminportal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_id', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=128, null=True)),
                ('skill', models.CharField(blank=True, max_length=128, null=True)),
                ('experience', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'candidate_skills',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecruiterAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(blank=True, max_length=45, null=True)),
                ('retype_password', models.CharField(blank=True, max_length=45, null=True)),
                ('contact_number', models.BigIntegerField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=55, null=True)),
                ('last_name', models.CharField(blank=True, max_length=55, null=True)),
                ('user_acc', models.CharField(max_length=55)),
                ('auth_group', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'recruiter_account',
                'managed': False,
            },
        ),
    ]
