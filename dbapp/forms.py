from django import forms
from .models import Employee,Inventory


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['id','name','aadhar','email','phone','address']
        
class InventoryForm(forms.ModelForm):
    class Meta: 
        model=Inventory
        fields=['inid','name','cost','quantity','quantity_sold','sales']

