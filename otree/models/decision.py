#!/usr/bin/env python
# -*- coding: utf-8 -*-
from otree.db import models


class Decision(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	component = models.CharField(max_length=100, null=False)
	session = models.CharField(max_length=100, null=False)
	subsession = models.IntegerField(null=False)
	round = models.IntegerField(null=False)
	group = models.IntegerField(null=False)
	participant = models.ForeignKey('otree.Participant', null=False)
	decision = models.JSONField(null=False)
