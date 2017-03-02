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
                ('in_all_groups_wait_page', otree.db.models.FloatField(default=0, null=True)),
                ('session', otree.db.models.ForeignKey(related_name='multi_player_game_group', to='otree.Session')),
            ],
            options={
                'db_table': 'multi_player_game_group',
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
                ('from_other_player', otree.db.models.PositiveIntegerField(null=True)),
                ('is_winner', otree.db.models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])),
                ('in_all_groups_wait_page', otree.db.models.FloatField(default=0, null=True)),
                ('group_id_before_p1_switch', otree.db.models.PositiveIntegerField(null=True)),
                ('group', otree.db.models.ForeignKey(to='multi_player_game.Group', null=True)),
                ('participant', otree.db.models.ForeignKey(related_name='multi_player_game_player', to='otree.Participant')),
                ('session', otree.db.models.ForeignKey(related_name='multi_player_game_player', to='otree.Session')),
            ],
            options={
                'db_table': 'multi_player_game_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('session', otree.db.models.ForeignKey(related_name='multi_player_game_subsession', to='otree.Session', null=True)),
            ],
            options={
                'db_table': 'multi_player_game_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=otree.db.models.ForeignKey(to='multi_player_game.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=otree.db.models.ForeignKey(to='multi_player_game.Subsession'),
        ),
    ]
