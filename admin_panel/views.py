from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def index(request):
    return render(request,"index.html")


def login(request):
    return render(request,"login.html")


def my_profile(request):
    return render(request,"my_profile.html")




def designation(request):
    designation = Designation.objects.all()
    return render(request,"masters/designation/designation.html",{"designations":designation})


def designation_add(request):
    if request.method == "POST":
        data = request.POST
        designation = data["designation"]
        if not Designation.objects.filter(name=designation).exists():
            p = Designation(name=designation)
            p.save()
            return redirect("designation")
        else:
            return HttpResponse("designation Already exist")
    return render(request,"masters/designation/designation_add.html")


def designation_edit(request,id):
    if request.method == "POST":
        data = request.POST
        text = data["designation"]
        p = Designation.objects.get(pk=id)
        p.name = text
        p.save()
        return redirect("designation")
    else:
        designation = Designation.objects.get(pk=id)
    return render(request,"masters/designation/designation_edit.html",{"designation":designation})




def place(request):
    places = Place.objects.all()
    
    return render(request,"masters/place/place.html",{"places":places})


def place_add(request):
    if request.method == "POST":
        data = request.POST
        place_name = data["placename"]
        # p = Place.objects.get(name=place_name)
        if not Place.objects.filter(name=place_name).exists():
            p = Place(name=place_name)
            p.save()
            return redirect("place")
        else:
            return HttpResponse("place Already exist")
    return render(request,"masters/place/place_add.html")


def place_edit(request,id):
    if request.method == "POST":
        data = request.POST
        place_name = data["placename"]
        place = Place.objects.get(pk=id)
        place.name = place_name
        place.save()
        return redirect("place")
    else:
        place = Place.objects.get(pk=id)
    return render(request,"masters/place/place_edit.html",{"place":place})





def holiday(request):
    holidays = Holiday.objects.all()
    return render(request,"masters/holiday/holiday.html",{"holidays":holidays})


def holiday_add(request):
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        reason = data["reason"]
        p = Holiday(reason=reason,holiday_date=date)
        p.save()
        return redirect("holiday")
        
    return render(request,"masters/holiday/holiday_add.html")


def holiday_edit(request,id):
    
    if request.method == "POST":
        data = request.POST
        reason = data["reason"]
        date = data["date"]
        holiday = Holiday.objects.get(pk=id)
        holiday.reason = reason
        holiday.holiday_date = date
        holiday.save()
        return redirect("holiday")
    else:
        holiday = Holiday.objects.get(pk=id)
    return render(request,"masters/holiday/holiday_edit.html",{"holiday":holiday})




def arp_items(request):
    products = ArpProduct.objects.all()
    services = ArpService.objects.all()
    return render(request,"masters/arp_items/arp_items.html",{"products":products,"services":services})



def product_edit(request,id):
    if request.method == "POST":
        data = request.POST
        productname = data["productname"]
        category = data["category"]
        hsn_code = data["hsn_code"]
        product_code = data["product_code"]
        sale_price = data["sale_price"]
        sale_price_with_tax = data["sale_price_with_tax"]
        purchase_price = data["purchase_price"]
        purchase_price_with_tax = data["purchase_price_with_tax"]
        tax_rate = data["tax_rate"]
        opening_stock = data["opening_stock"]
        price_per_unit = data["price_per_unit"]
        date = data["date"]
        minimum_stock_quantity = data["minimum_stock_quantity"]
        unit = data["unit"]

        p = ArpProduct.objects.get(pk=id)
        p.name = productname
        p.category = category
        p.hsn_code = hsn_code
        p.product_code = product_code
        p.sale_price = sale_price
        p.sale_price_with_tax = sale_price_with_tax
        p.purchase_price = purchase_price
        p.purchase_price_with_tax = purchase_price_with_tax
        p.tax_rate = tax_rate
        p.opening_stock = opening_stock
        p.price_per_unit = price_per_unit
        p.date = date
        p.minimum_stock_quantity = minimum_stock_quantity
        p.unit = unit
        p.save()
        return redirect("arp_items")
    else:
        product = ArpProduct.objects.get(pk=id)
    return render(request,"masters/arp_items/product_edit.html",{"product":product})



def bank_list(request):
    bank_list = BankAccount.objects.all()
    return render(request,"masters/bank/bank_list.html",{"bank_list":bank_list})


def bank_add(request):
    if request.method == "POST":
        data = request.POST
        name = data['name']
        balance = data['balance']
        date = data['date']
        b = BankAccount(name=name,balance=balance,as_on=date)
        b.save()
        return redirect("bank_list")
    return render(request,"masters/bank/bank_add.html")




def expense_category(request):
    category = ExpenseCategory.objects.all()
    
    return render(request,"masters/expense_category/expense_category.html",{"category":category})


def expense_category_edit(request,id):
    
    if request.method == "POST":
        data = request.POST
        expname = data["category"]
        expense_type = data["expense_type"]
        p = ExpenseCategory.objects.get(pk=id)
        p.reason = expname
        p.expenseType = expense_type
        p.save()
        return redirect("expense_category")
    else:
        category = ExpenseCategory.objects.get(pk=id)
    
    return render(request,"masters/expense_category/expense_category_edit.html",{"category":category})












def my_customer(request):
    return render(request,"my_customer.html")


def add_customer(request):
    return render(request,"add_customer.html")


def place_order(request):
    return render(request,"place_order.html")


def cancel_order(request):
    return render(request,"cancel_order.html")


def view_place_order(request):
    return render(request,"view_place_order.html")


def party_details(request):
    return render(request,"party_details.html")


def party_ledger(request):
    return render(request,"party_ledger.html")


def cylinder_delivery_report(request):
    return render(request,"cylinder_delivery_report.html")


def cancel_order_report(request):
    return render(request,"cancel_order_report.html")


def add_place_order(request):
    return render(request,"add_place_order.html")


