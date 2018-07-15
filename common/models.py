# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BigLottery(models.Model):
    volume = models.TextField(primary_key=True) 
    date = models.TextField()
    no1 = models.IntegerField()
    no2 = models.IntegerField()
    no3 = models.IntegerField()
    no4 = models.IntegerField()
    no5 = models.IntegerField()
    no6 = models.IntegerField()
    special = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Big_Lottery'


class MyLottery(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.TextField()
    volume = models.TextField()
    date = models.TextField()
    no1 = models.IntegerField()
    no2 = models.IntegerField()
    no3 = models.IntegerField()
    no4 = models.IntegerField()
    no5 = models.IntegerField()
    no6 = models.IntegerField()
    no7 = models.IntegerField()
    no8 = models.IntegerField()
    no9 = models.IntegerField()
    no10 = models.IntegerField()
    no11 = models.IntegerField()
    no12 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'My_Lottery'


class TwoWin(models.Model):
    volume = models.TextField(primary_key=True)
    date = models.TextField()
    no1 = models.IntegerField()
    no2 = models.IntegerField()
    no3 = models.IntegerField()
    no4 = models.IntegerField()
    no5 = models.IntegerField()
    no6 = models.IntegerField()
    no7 = models.IntegerField()
    no8 = models.IntegerField()
    no9 = models.IntegerField()
    no10 = models.IntegerField()
    no11 = models.IntegerField()
    no12 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Two_Win'
