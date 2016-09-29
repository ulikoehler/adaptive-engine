# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequenceitem',
            name='activity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='module.Activity'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='sequenceitem',
            unique_together=set([('user_module', 'position')]),
        ),
    ]
