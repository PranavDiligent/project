
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("login",views.login, name="login"),
    path("my_profile/",views.my_profile, name="my_profile"),

  


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
    
    
    # path("designation/",views.designation,name="designation"),
    path("designation/",views.designation, name="designation"),
    path("designation_add/",views.designation_add, name="designation_add"),
    path("designation_edit/<int:id>",views.designation_edit, name="designation_edit"),
    
    path("place/",views.place,name="place"),
    path("place_add/",views.place_add,name="place_add"),
    path("place_edit/<int:id>",views.place_edit,name="place_edit"),

    path("holiday/",views.holiday,name="holiday"),
    path("holiday_add/",views.holiday_add,name="holiday_add"),
    path("holiday_edit/<int:id>",views.holiday_edit,name="holiday_edit"),
   
   
    path("arp_items/",views.arp_items,name="arp_items"),
    path("holiday_add/",views.holiday_add,name="holiday_add"),
    path("product_edit/<int:id>",views.product_edit,name="product_edit"),


    path("bank_list/",views.bank_list,name="bank_list"),
    path("bank_add/",views.bank_add,name="bank_add"),


    path("expense_category/",views.expense_category,name="expense_category"),
    path("expense_category_edit/<int:id>",views.expense_category_edit,name="expense_category_edit"),




]
