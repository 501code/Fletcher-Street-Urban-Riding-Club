from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class SiteDetail(models.Model):
    label = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=400)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.label

    def __unicode__(self):
        return unicode(self.value)
