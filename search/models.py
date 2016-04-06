from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Searchdata(models.Model):
    string_text = models.CharField(max_length=200)
    def __str__(self):
        return self.string_text
