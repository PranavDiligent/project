from django.contrib import admin
from .models import *
# Register your models here.

myModels = [Designation,Place,Holiday,Category,BankAccount,ExpenseItem,ExpenseCategory,ArpProduct,ArpService]
admin.site.register(myModels)