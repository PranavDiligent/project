
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("login",views.login, name="login"),
    path("my_profile/",views.my_profile, name="my_profile"),

    path("my_zone/",views.my_zone, name="my_zone"),
    path("my_customer/",views.my_customer, name="my_customer"),
    path("add_customer/",views.add_customer, name="add_customer"),

    path("place_order/",views.place_order, name="place_order"),
    path("add_place_order/",views.add_place_order, name="add_place_order"),
    path("view_place_order/",views.view_place_order, name="view_place_order"),
    path("cancel_order/",views.cancel_order, name="cancel_order"),

    path("cancel_order_report/",views.cancel_order_report, name="cancel_order_report"),
    
    path("party_ledger/",views.party_ledger, name="party_ledger"),
    path("party_details/",views.party_details, name="party_details"),
    
    path("cylinder_delivery_report/",views.cylinder_delivery_report, name="cylinder_delivery_report"),
    
    
]
