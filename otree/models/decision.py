#!/usr/bin/env python
# -*- coding: utf-8 -*-
from otree.db import models
from django.utils import timezone


class Decision(models.Model):

    class Meta:
        app_label = "otree"
        # If I don't set this, it could be in an unpredictable order
        ordering = ['pk']

    timestamp = models.DateTimeField(null=False)
    component = models.CharField(max_length=100, null=False)
    session = models.ForeignKey(
        'otree.Session',
        null=False,
        related_name='+')
    subsession = models.IntegerField(null=True)
    round = models.IntegerField(null=False)
    group = models.IntegerField(null=False)
    page = models.CharField(max_length=100, null=False)
    app = models.CharField(max_length=100, null=False)
    participant = models.ForeignKey('otree.Participant', null=False)
    decision_vector = models.JSONField(null=False)

    def save(self, *args, **kwargs):
        if self.timestamp is None:
            self.timestamp = timezone.now()
        super(Decision, self).save(*args, **kwargs)