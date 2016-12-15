from __future__ import unicode_literals
from django.db import models
import re

class User(models.Model):
    email = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()


class UserManager(models.Manager):
    def validate(self, email):
        validator = re.compile("^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
        if validator.match(email)
            return true
        else:
            return false
