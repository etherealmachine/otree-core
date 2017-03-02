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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', otree.db.models.DateTimeField(null=True)),
                ('component', otree.db.models.CharField(max_length=100, null=True)),
                ('subsession', otree.db.models.IntegerField(null=True)),
                ('round', otree.db.models.IntegerField(null=True)),
                ('group', otree.db.models.IntegerField(null=True)),
                ('page', otree.db.models.CharField(max_length=100, null=True)),
                ('app', otree.db.models.CharField(max_length=100, null=True)),
                ('decision_vector', otree.db.models.JSONField(null=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='LogEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', otree.db.models.DateTimeField(auto_now_add=True, null=True)),
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
            model_name='logevent',
            name='session',
            field=otree.db.models.ForeignKey(related_name='+', to='otree.Session'),
        ),
        migrations.AddField(
            model_name='decision',
            name='participant',
            field=otree.db.models.ForeignKey(to='otree.Participant'),
        ),
        migrations.AddField(
            model_name='decision',
            name='session',
            field=otree.db.models.ForeignKey(related_name='+', to='otree.Session'),
        ),
    ]
