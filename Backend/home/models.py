from django.db import models

class faq(models.Model):
    question=models.CharField(max_length=150)
    answer=models.TextField()

    def __str__(self):
        return self.question

class Category(models.Model):
    sub_category=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='sub_cat')
    sub=models.BooleanField(default=False)
    name=models.CharField(max_length=200)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='category',null=True,blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ManyToManyField(Category)
    name=models.CharField(max_length=200)
    information=models.TextField(blank=True,null=True)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Forms(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    store_name=models.CharField(max_length=100,blank=True)
    job=models.CharField(max_length=100,blank=True)
    management=models.CharField(max_length=100,blank=True)
    media_address=models.CharField(max_length=100,blank=True)
    mobile=models.IntegerField(default=1,blank=True)
    landline=models.IntegerField(default=1,blank=True)
    quantity=models.PositiveIntegerField(default=0,blank=True)
    material=models.CharField(max_length=100,blank=True)
    information=models.TextField(blank=True)
    length=models.PositiveIntegerField(default=10,blank=True)
    width=models.PositiveIntegerField(default=10,blank=True)



"""class offsetForm(models.Model):
    store_name=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    management=models.CharField(max_length=100)
    media_address=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    landline=models.CharField(max_length=100)

class sublimitionForm(models.Model):
    quantity=models.PositiveIntegerField(null=True,blank=True)
    material=models.CharField(max_length=100)
    information=models.TextField()
    length=models.PositiveIntegerField()
    width=models.PositiveIntegerField()"""