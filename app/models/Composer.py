
from django.db import models

from app.models.damn import Model


class Composer(models.Model, Model):
    cid = models.BigIntegerField(primary_key=True)
    banner = models.CharField(max_length=512)
    avatar = models.CharField(max_length=512)
    verified = models.IntegerField()
    name = models.CharField(max_length=128)
    intro = models.TextField(blank=True, null=True)
    like_counts = models.IntegerField()
    fans_counts = models.IntegerField()
    follow_counts = models.IntegerField()
    location = models.CharField(max_length=32, blank=True, null=True)
    career = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'composers'


