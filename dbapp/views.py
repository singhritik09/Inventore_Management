from urllib import request
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import is_valid_path
from matplotlib.style import context
from requests import delete
from .models import Employee ,Inventory
from .forms import EmployeeForm, InventoryForm,UpdateInventoryForm

from django.contrib import messages


# Create your views here.

def index(request):
    all_employee=Employee.objects.all()
    
    return render(request,'index.html',{'all':all_employee})

def test(request):
    check= Employee.objects.filter(id=2)
    return render(request,'test.html',{'ts':check})

def add(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST or None)
        if form.is_valid():
            form.save()
            
        messages.success(request,('New Employee Added to database'))
        return redirect('index')
        # return render(request,'add.html',{})
    else:
        return render(request,'add.html',{})

def add_inventory(request):
    
    if request.method=='POST':
        form=InventoryForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,('Item successfully added to Inventory'))
        return redirect('inventory')
    else:
        return render(request,'add_inventory.html',{})

def inventory(request):
    inventories=Inventory.objects.all()
    context={
        "title": "Inventory List",
        "inventories": inventories
    }
    return render(request,'inventory.html',context=context)

def product(request,pk):
    
    inventory=get_object_or_404(Inventory, pk=pk)
    
    context={
        'inventory':inventory
    }
    return render(request,"product.html",context=context)

def delete_inventory(request,pk):
    inventory=get_object_or_404(Inventory,pk=pk)
    inventory.delete()
    
    return redirect('inventory')

def update_inventory(request, pk):
    inventory=get_object_or_404(Inventory,pk=pk)
    if request.method =='POST':
        form=UpdateInventoryForm(data=request.POST)
        if form.is_valid():
            inventory.name=form.data['name']
            inventory.cost=form.data['cost']
            inventory.quantity=form.data['quantity']
            inventory.quantity_sold=form.data['quantity_sold']
            inventory.sales=form.data['sales']
        
            inventory.save()
        
            messages.success(request,("Updated Inventory"))
            return redirect('product/{pk}')
    else:
        
        return render(request,'update_inventory.html',{})