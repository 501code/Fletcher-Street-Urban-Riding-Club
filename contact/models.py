from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    subject = models.CharField('Subject', max_length=100)
    name = models.CharField('Full Names', max_length=100)
    email = models.EmailField('Email')
    body = models.TextField('Body', max_length=5000)
    cc_myself = models.BooleanField('CC Sender', default=False)

    def __str__(self):
        return self.subject