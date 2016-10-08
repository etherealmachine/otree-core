#!/usr/bin/env python
# -*- coding: utf-8 -*-
from otree.db import models


class Decision(models.Model):

	class Meta:
		app_label = "otree"
		# if i don't set this, it could be in an unpredictable order
		ordering = ['pk']

	timestamp = models.DateTimeField(auto_now_add=True)
	component = models.CharField(max_length=100, null=False)
	session = models.CharField(max_length=100, null=False)
	subsession = models.IntegerField(null=True)
	round = models.IntegerField(null=False)
	group = models.IntegerField(null=False)
	participant = models.ForeignKey('otree.Participant', null=False)
	decision = models.JSONField(null=False)
