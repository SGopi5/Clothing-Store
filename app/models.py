from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    desc=models.TextField(max_length=200)
    phone=models.IntegerField()


    def __str__(self):
        return self.name


class Product(models.Model):
    Product_ID=models.AutoField
    Product_Name=models.CharField( max_length=50)
    Product_Category=models.CharField(max_length=50 ,default="")
    Product_SubCategory=models.CharField(max_length=50)
    Product_Price=models.IntegerField(default=0)
    Product_Desc=models.CharField(max_length=300)
    Product_Image=models.ImageField(upload_to='images/image', height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.Product_Name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json =  models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    oid=models.CharField(max_length=150,blank=True)
    amountpaid=models.CharField(max_length=500,blank=True,null=True)
    paymentstatus=models.CharField(max_length=20,blank=True)
    phone = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.name
    

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    delivered=models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."