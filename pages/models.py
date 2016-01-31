from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Section(models.Model):
    title = models.CharField('Section Title', max_length=300)
    description = models.CharField('Description', max_length=400)
    key = models.CharField(max_length=50)
    pub_date = models.DateTimeField('Date Published', default=timezone.now)
    visible = models.BooleanField('Visible', default=True)

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField('Page Title', max_length=300)
    body = models.TextField('Body', max_length=5000)
    published = models.BooleanField('Published', default=True)
    pub_date = models.DateTimeField('Date Published', default=timezone.now)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
