# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('otree', '0011_auto_20160805_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_is_missing_players', otree.db.models.BooleanField(default=False, db_index=True, choices=[(True, 'Yes'), (False, 'No')])),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('min_max', otree.db.models.CurrencyField(null=True, max_digits=12)),
                ('dynamic_min_max', otree.db.models.CurrencyField(null=True, max_digits=12)),
                ('in_before_session_starts', otree.db.models.CurrencyField(null=True, max_digits=12)),
                ('session', otree.db.models.ForeignKey(related_name='single_player_game_group', to='otree.Session')),
            ],
            options={
                'db_table': 'single_player_game_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_in_group', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('payoff', otree.db.models.CurrencyField(null=True, max_digits=12)),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('blank', otree.db.models.CharField(max_length=500, null=True, blank=True)),
                ('add100_1', otree.db.models.PositiveIntegerField(null=True)),
                ('add100_2', otree.db.models.PositiveIntegerField(null=True)),
                ('even_int', otree.db.models.PositiveIntegerField(null=True)),
                ('after_next_button_field', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('dynamic_choices', otree.db.models.CharField(max_length=500, null=True)),
                ('dynamic_min_max', otree.db.models.CurrencyField(null=True, max_digits=12)),
                ('in_before_session_starts', otree.db.models.CurrencyField(null=True, max_digits=12)),
                ('group', otree.db.models.ForeignKey(to='single_player_game.Group', null=True)),
                ('participant', otree.db.models.ForeignKey(related_name='single_player_game_player', to='otree.Participant')),
                ('session', otree.db.models.ForeignKey(related_name='single_player_game_player', to='otree.Session')),
            ],
            options={
                'db_table': 'single_player_game_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('session', otree.db.models.ForeignKey(related_name='single_player_game_subsession', to='otree.Session', null=True)),
            ],
            options={
                'db_table': 'single_player_game_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=otree.db.models.ForeignKey(to='single_player_game.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=otree.db.models.ForeignKey(to='single_player_game.Subsession'),
        ),
    ]
