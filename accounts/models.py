# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    contrib     = models.BooleanField(default=False)
    
    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)