from django.db import models

# Create your models here.

class Designation(models.Model):

    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class Place(models.Model):

    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name



class Holiday(models.Model):

    holiday_date = models.DateField(auto_now=False, auto_now_add=False)
    reason = models.CharField(max_length=100)

    def __str__(self):
        return self.reason


class Category(models.Model):

    name = models.CharField( max_length=100,unique=True)

    def __str__(self):
        return self.name


class Gst(models.Model):

    name = models.CharField( max_length=50)
    tax_value = models.DecimalField( max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name




class ArpProduct(models.Model):

    taxTypes = (
        ('withTax','with Tax'),
        ('withoutTax','without Tax'),
    )

    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)
    hsn_code = models.IntegerField()
    product_code = models.CharField(max_length=100)
    sale_price = models.CharField(max_length=100)
    sale_price_type = models.CharField(choices=taxTypes ,max_length=50)
    purchase_price = models.CharField(max_length=100)
    purchase_price_type = models.CharField(choices=taxTypes ,max_length=50)
    tax_rate = models.ForeignKey("Gst", on_delete=models.CASCADE)
    opening_stock = models.CharField(max_length=100)
    price_per_unit = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    minimum_stock_quantity = models.IntegerField()
    unit = models.IntegerField()

    def __str__(self):
        return self.name


class ArpService(models.Model):
    taxTypes = (
            ('withTax','with Tax'),
            ('withoutTax','without Tax'),
        )
    name = models.CharField(max_length=100)
    hsn_code = models.CharField(max_length=100)
    sale_price = models.CharField(max_length=100)
    sale_price_type = models.CharField( choices=taxTypes,max_length=50)
    tax_rate = models.ForeignKey("Gst", on_delete=models.CASCADE)

    def __str__(self):
        return self.name





class PrpService(models.Model):

    name = models.CharField(max_length=100)
    hsn_code = models.CharField(max_length=100)
    service_code = models.CharField( max_length=50)
    service_price = models.IntegerField()
    
    def __str__(self):
        return self.name



class ArpParty(models.Model):

    name = models.CharField( max_length=100)
    phone = models.CharField( max_length=100)
    address = models.CharField( max_length=100)
    email = models.EmailField( max_length=254)
    state = models.CharField( max_length=100)
    date = models.DateField( auto_now=False, auto_now_add=False)
    opening_balance = models.CharField( max_length=100)
    gst_number = models.CharField( max_length=100)

    def __str__(self):
        return self.name

    
class PrpParty(models.Model):

    name = models.CharField( max_length=100)
    phone = models.CharField( max_length=100)
    address = models.CharField( max_length=100)
    email = models.EmailField( max_length=254)
    state = models.CharField( max_length=100)
    date = models.DateField( auto_now=False, auto_now_add=False)
    opening_balance = models.CharField( max_length=100)
    gst_number = models.CharField( max_length=100)
    
    def __str__(self):
        return self.name


class BankAccount(models.Model):

    name = models.CharField( max_length=100)
    balance = models.CharField( max_length=100)
    as_on = models.DateField( auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.name

    
class ExpenseItem(models.Model):

    name = models.CharField( max_length=100,unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class ExpenseCategory(models.Model):

    expenseTypes = (
        ('indirectExpense','indirect Expense'),
        ('directExpense','direct Expense'),
    )

    name = models.CharField( max_length=100,unique=True)
    expenseType = models.CharField(choices=expenseTypes,max_length=50)

    def __str__(self):
        return self.name
