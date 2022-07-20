from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")


def login(request):
    return render(request,"login.html")


def my_profile(request):
    return render(request,"my_profile.html")


def my_zone(request):
    return render(request,"my_zone.html")


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


