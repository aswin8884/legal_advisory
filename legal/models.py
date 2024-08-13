from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Login_table(AbstractUser):
    usertype=models.CharField(max_length=25)

class User_registration(models.Model):
    name=models.CharField(max_length=50,null=True)
    contact=models.IntegerField(null=True)
    address=models.CharField(max_length=250,null=True)
    gender=models.CharField(max_length=25,null=True)
    id_proof=models.FileField(null=True)
    profile_picture=models.ImageField(null=True)
    email=models.EmailField(null=True)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)

class Advocate_registration(models.Model):
    name=models.CharField(max_length=50,null=True)
    contact=models.IntegerField(null=True)
    address=models.CharField(max_length=250,null=True)
    gender=models.CharField(max_length=25,null=True)
    email=models.EmailField(null=True)
    advocate_type=models.CharField(max_length=25,null=True)
    id_proof=models.FileField(null=True)
    degree_cerificate=models.FileField(null=True)
    licence=models.FileField(null=True)
    profile_picture=models.ImageField(null=True)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)
    approved = models.BooleanField(default=False)
    fees=models.IntegerField(default=0)
    cases_won=models.IntegerField(default=0)

class Ipc_section(models.Model):
    section_name=models.CharField(max_length=25,null=True)
    description=models.CharField(max_length=250,null=True)
    punishment=models.CharField(max_length=250,null=True)

class Messages(models.Model):
    advocate_id=models.ForeignKey(Advocate_registration,on_delete=models.CASCADE,null=True)
    user_id=models.ForeignKey(User_registration,on_delete=models.CASCADE,null=True)
    case=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=500,null=True)
    current_date=models.DateField(null=True)
    accepted_date=models.DateField(null=True)
    status=models.BooleanField(null=True)

class Cases(models.Model):
    user_id=models.ForeignKey(User_registration,on_delete=models.CASCADE,null=True)
    advocate_id=models.ForeignKey(Advocate_registration,on_delete=models.CASCADE,null=True)
    case=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=500,null=True)
    image=models.ImageField(null=True)
    posted_date=models.DateField(null=True)
    accepted_date_user=models.DateField(null=True)
    status=models.BooleanField(null=True,default=False)

class Request_work_admin(models.Model):
    case_id=models.ForeignKey(Cases,on_delete=models.CASCADE,null=True)
    advocate_id=models.ForeignKey(Advocate_registration,on_delete=models.CASCADE,null=True)
    status=models.BooleanField(null=True,default=False)
    approval=models.BooleanField(null=True,default=False)
    accepted_date=models.DateField(null=True)
    accepted_date_user=models.DateField(null=True)

class Feedbacks(models.Model):
    advocate_id=models.ForeignKey(Advocate_registration,on_delete=models.CASCADE,null=True)
    user_id=models.ForeignKey(User_registration,on_delete=models.CASCADE,null=True)
    rating=models.IntegerField(null=True)
    feedback=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=500,null=True)
    posted_date=models.DateField()

    