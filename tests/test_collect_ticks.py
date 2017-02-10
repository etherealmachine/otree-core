#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import random

from django.core.management import call_command
from django.utils import timezone

from otree.firebase.ticks import collect_ticks
from otree.models.decision import Decision
from otree.models.log import LogEvent
from otree.models.participant import Participant
from otree.session import SESSION_CONFIGS_DICT

from .base import TestCase


class TestCollectTicks(TestCase):

  def test_collect_ticks(self):
    for session in range(2):
      session_start_time = timezone.now() + datetime.timedelta(hours=session)
      session_name = 'multi_player_game'
      session_conf = SESSION_CONFIGS_DICT[session_name]
      npar = session_conf["num_demo_participants"]
      call_command('create_session', session_name, str(npar))

      players = Participant.objects.all()
      for roundno in range(2):
        # Create some decision points spread out over
        # 10 seconds into the future.
        offset_millis = 0
        for i in range(10):
          d = Decision()
          d.timestamp = session_start_time + datetime.timedelta(milliseconds=offset_millis)
          d.component = 'test-component'
          d.session = 'test-session-{}'.format(session)
          d.subsession = 0
          d.round = roundno
          d.group = 0
          d.participant = random.choice(players)
          d.app = 'test-app'
          d.page = 'test-page'
          d.decision = {}
          for player in players:
            d.decision[player.code] = 0.5
          d.save()
          offset_millis += random.randint(100, 1000)

    expected_ticks = []
    for session in range(2):
      for roundno in range(2):
        for tick in range(10):
          for player in players:
            expected_ticks.append({
              'tick': tick,
              'participant': player.code,
              'decision': 0.5,
              'session': 'test-session-{}'.format(session),
              'subsession': 0,
              'round': roundno,
              'group': 0
            })

    actual_header, actual_ticks = collect_ticks(Decision.objects.all())
    # Quick test for length equality - assertEqual takes a very long
    # time to compare non-equal large lists.
    if len(actual_ticks) != len(expected_ticks):
      raise AssertionError(
        '{} != {}'.format(len(actual_ticks), len(expected_ticks)))
    else:
      self.assertEqual(actual_ticks, expected_ticks)