from django.db import models
from django.contrib.auth.models import User

class capitalTypes(models.Model):
    class Meta:
        verbose_name = "Algorithm name"
        verbose_name_plural = "Algorithm names"
    name = models.CharField(max_length=300, default="", blank=True)

    def __str__(self):
        return f'{self.name}'


class CapitalType(models.Model):
    namec = models.ForeignKey(capitalTypes, on_delete=models.CASCADE,null=True)
    matrix_weights = models.JSONField(blank=True, default=list, null=True)
    counterlist = models.JSONField(blank=True, default=list, null=True)
    counter = models.IntegerField(default=0, null=True)
    status = models.BooleanField(default=0, null=True)

    def __str__(self):
        return (f'{self.namec.name} : {self.counter}')
