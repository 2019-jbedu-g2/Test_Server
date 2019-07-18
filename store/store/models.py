# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accountdb(models.Model):
    storenum = models.ForeignKey('Storedb', models.DO_NOTHING, db_column='storenum')
    storeid = models.CharField(primary_key=True, max_length=20)
    storepwd = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'accountdb'


class Queuedb(models.Model):
    barcode = models.CharField(primary_key=True, max_length=20)
    onoffline = models.BooleanField()
    storenum = models.ForeignKey('Storedb', models.DO_NOTHING, db_column='storenum')
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'queuedb'


class Storedb(models.Model):
    storenum = models.CharField(primary_key=True, max_length=10)
    storename = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    latitude = models.CharField(max_length=40)
    longitude = models.CharField(max_length=40)
    intro = models.CharField(max_length=200, blank=True, null=True)
    menu = models.CharField(max_length=300, blank=True, null=True)
    inform = models.CharField(max_length=500, blank=True, null=True)
    latencytime = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'storedb'
