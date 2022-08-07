# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from statistics import mode
from tkinter.tix import Balloon
from django.db import models
import django.db
class Employee(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    aadhar=models.IntegerField(unique=True,null=False,)
    email = models.CharField(max_length=25, blank=False, null=False)
    phone = models.BigIntegerField(max_length=10,blank=False, null=False)
    address=models.CharField(max_length=150,blank=False,null=False)
    
    
    class Meta:
        managed = False
        db_table = 'Employee'
    # def __str__(self):
    #     return self.name
    
        # query = 'SELECT * FROM employee
        
        
class Inventory(models.Model):
    inid=models.IntegerField(primary_key=True,unique=True)
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
        
        
# class Managers(models.Model):
#     id = models.ForeignKey(Employee,null=False)
#     name=models.ForeignKey(Employee,null=False)
#     field=models.CharField(max_length=50,null=False)
    
#     class Meta:
#         managed=False
#         db_table='Managers'



# class Marble(models.Model):
#     id = models.IntegerField(primary_key=True,null=False)
#     name=models.CharField(max_length=50,null=False)
#     cost=models.IntegerField(null=False)
#     type=models.ForeignKey(Inventory,null=False)
#     quantity=models.IntegerField(null=False)
    
#     class Meta:
#         managed=False
#         db_table='Marble'
        
# class Granite(models.Model):
#     id=models.IntegerField(primary_key=True)
#     name=models.CharField(max_length=50,null=False)
#     cost=models.IntegerField(null=False)
#     type=models.ForeignKey(Inventory,null=False)
    
#     class Meta:
#         managed=False
#         db_table='Granite'
        
        