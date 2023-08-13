from django.db import models

class service(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
    description2=models.TextField(default=None,blank=True,null=True)
    pic1=models.ImageField(upload_to="service")
    pic2=models.ImageField(upload_to="service",default=None,null=True,blank=True)
    pic3=models.ImageField(upload_to="service",default=True,null=True,blank=True)
    pic4=models.ImageField(upload_to="service",default=True,null=True,blank=True)
    pic5=models.ImageField(upload_to="service",default=True,null=True,blank=True)
    def __str__(self):
        return str(self.id) +"-"+ self.name 

class team(models.Model):
    id=models.AutoField(primary_key=True)
    pic=models.ImageField(upload_to="team")
    name=models.CharField(max_length=80)
    profession=models.CharField(max_length=100)
    def __str__(self):
        return str(self.id) +"-"+ self.name 

class testimonial(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=80)
    profession=models.CharField(max_length=100)
    message=models.TextField()
    pic=models.ImageField(upload_to="experience",default=None,blank=True,null=True)
    def __str__(self):
        return str(self.id) +"-"+ self.name 

class quote(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=80)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    service=models.CharField(max_length=100)
    message=models.TextField(default=None,blank=True,null=True)
    def __str__(self):
        return str(self.id) +"-"+ self.name 
    
class contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=80)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=100)
    message=models.TextField(default=None,blank=True,null=True)
    def __str__(self):
        return str(self.id) +"-"+ self.name 
