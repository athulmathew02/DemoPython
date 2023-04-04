from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.


class district(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class branch(models.Model):
    distid = models.ForeignKey(district, on_delete=CASCADE)
    branchname = models.CharField(max_length=100)

    def __str__(self):
        return self.branchname
