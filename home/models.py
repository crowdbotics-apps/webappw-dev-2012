from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    temp = models.BigIntegerField(null=True, blank=True,)
    temp2 = models.BigIntegerField(null=True, blank=True,)
    temp3 = models.BigIntegerField(null=True, blank=True,)
    csc = models.BigIntegerField(null=True, blank=True,)
    temp4 = models.BigIntegerField(null=True, blank=True,)
    temp5 = models.BigIntegerField(null=True, blank=True,)
    temp6 = models.BigIntegerField(null=True, blank=True,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Test(models.Model):
    "Generated Model"
    test = models.BigIntegerField()
