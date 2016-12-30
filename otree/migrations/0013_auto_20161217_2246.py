# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('otree', '0012_auto_20161020_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='decision',
            name='app',
            field=otree.db.models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='decision',
            name='page',
            field=otree.db.models.CharField(max_length=100, null=True),
        ),
    ]
