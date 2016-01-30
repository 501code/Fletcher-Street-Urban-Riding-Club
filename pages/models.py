from __future__ import unicode_literals

from django.db import models


class Page(models.Model):
    title = models.CharField('Page Title', max_length=100)
    body = models.TextField('Body', max_length=5000)
    pub_date = models.DateField('Date Published',)

    def __str__(self):
        return self.title