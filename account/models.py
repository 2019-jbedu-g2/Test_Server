from django.db import models

# Create your models here.


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
    createtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True, blank=True, null=True)
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