from django.db import models
from django.contrib import admin

class Name(models.Model):
    name = models.CharField(max_length=200)
    
    @admin.display(
        boolean=True,
        ordering='name',
        description='Generated names',
    )

    def __str__(self):
        return self.name