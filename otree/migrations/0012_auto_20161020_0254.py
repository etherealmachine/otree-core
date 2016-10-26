# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('otree', '0011_auto_20160805_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decision',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('timestamp', otree.db.models.DateTimeField(auto_now_add=True, null=True)),
                ('component', otree.db.models.CharField(null=True, max_length=100)),
                ('session', otree.db.models.CharField(null=True, max_length=100)),
                ('subsession', otree.db.models.IntegerField(null=True)),
                ('round', otree.db.models.IntegerField(null=True)),
                ('group', otree.db.models.IntegerField(null=True)),
                ('decision', otree.db.models.JSONField(null=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='LogEvent',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('timestamp', otree.db.models.DateTimeField(auto_now_add=True, null=True)),
                ('session', otree.db.models.CharField(null=True, max_length=100)),
                ('subsession', otree.db.models.IntegerField(null=True)),
                ('round', otree.db.models.IntegerField(null=True)),
                ('group', otree.db.models.IntegerField(null=True)),
                ('event', otree.db.models.JSONField(null=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.AlterModelOptions(
            name='participant',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ['pk']},
        ),
        migrations.AlterIndexTogether(
            name='participant',
            index_together=set([('session', 'mturk_worker_id', 'mturk_assignment_id')]),
        ),
        migrations.AddField(
            model_name='logevent',
            name='participant',
            field=otree.db.models.ForeignKey(to='otree.Participant'),
        ),
        migrations.AddField(
            model_name='decision',
            name='participant',
            field=otree.db.models.ForeignKey(to='otree.Participant'),
        ),
    ]
