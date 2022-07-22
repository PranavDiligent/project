from django.contrib import admin
from .models import *
# Register your models here.

myModels = [Designation,Place,Gst,Holiday,Category,BankAccount,ArpParty,PrpParty,
ExpenseItem,ExpenseCategory,ArpProduct,ArpService]
admin.site.register(myModels)