# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First name', max_length=100)),
                ('middle_name', models.CharField(help_text='Middle name', max_length=100)),
                ('last_name', models.CharField(help_text='Last name', max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
    ]
