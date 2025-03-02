from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)
    message = models.TextField()  # Ensure this field exists
    

    def  __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=500)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.TextField()  # Better for longer descriptions

    image = models.ImageField(upload_to='img/images/', default='img/default.jpg')  # Provide a valid default image

    def __str__(self):
        return self.product_name


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



class Blog(models.Model):
    title = models.CharField(max_length=255)  # Title of the blog post
    description = models.TextField()  # Short description or excerpt of the post
    content = models.TextField()  # Full content of the blog post
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)  # Image for the post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the post is created

    def __str__(self):
        return self.title



class Review(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='review_images/', blank=True, null=True)
    review_text = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}⭐"