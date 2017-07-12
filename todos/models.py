# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.urlresolvers import reverse

# Token-based Authentication
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# from django.conf import settings


class Todo(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='+')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    to_be_completed = models.DateField(default=datetime.now)
    is_achieved = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('todo:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + ' - ' + self.text


# Token-based Authentication
# This code is triggered whenever a new user has been created and saved to the database

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
