#!/usr/bin/env python
# -*- coding: utf-8 -*-
from otree.db import models


class LogEvent(models.Model):

	class Meta:
	    app_label = "otree"
	    # if i don't set this, it could be in an unpredictable order
	    ordering = ['pk']

	timestamp = models.DateTimeField(auto_now_add=True)
	session = models.CharField(max_length=100, null=False)
	subsession = models.IntegerField(null=False)
	round = models.IntegerField(null=False)
	group = models.IntegerField(null=False)
	participant = models.ForeignKey('otree.Participant', null=False)
	event = models.JSONField(null=False)
