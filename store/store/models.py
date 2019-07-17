# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Storedb(models.Model):
    storenum = models.CharField(primary_key=True, max_length=10)
    storename = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    coordinates = models.CharField(max_length=40)
    intro = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    phonenum = models.CharField(max_length=15, blank=True, null=True)
    menu = models.CharField(max_length=300, blank=True, null=True)
    inform = models.CharField(max_length=300, blank=True, null=True)
    openclose = models.CharField(max_length=10)
    latencytime = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'storedb'
