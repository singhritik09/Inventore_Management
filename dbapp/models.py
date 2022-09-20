from tabnanny import check
from tkinter.tix import Balloon
from django.db import models
import django.db


class Department(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=25, blank=True, null=True)
    location = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    aadhar = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Inventory(models.Model):
    inid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100,null=False,blank=False)
    cost=models.IntegerField(null=False)
    quantity=models.IntegerField(null=False,blank=False)
    quantity_sold=models.IntegerField(null=False,blank=False)
    sales=models.IntegerField(null=False,blank=False)
    stock_date=models.DateField(auto_now_add=True,null=True)
    last_sale=models.DateField(auto_now_add=True,null=True)
    
    
    class Meta:
        managed=False
        db_table='Inventory'
        
        

class Managers(models.Model):
    id = models.OneToOneField(Employee, models.DO_NOTHING, db_column='id', primary_key=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'managers'


