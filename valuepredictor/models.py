from django.db import models

# Create your models here.


class InputModel(models.Model):
    info = models.CharField(max_length=400, null=False)