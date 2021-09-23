from django.db import models

class Name(models.Model):
    adjective = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    