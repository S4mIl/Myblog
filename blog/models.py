from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name



class Blog(models.Model):
   
    name=models.CharField(max_length=200,unique=True)
    category=models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    tags=models.ManyToManyField(Tag,blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='blog/%Y/%m/%d')
    available=models.BooleanField(default=True)
    date=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name