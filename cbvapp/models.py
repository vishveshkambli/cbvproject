from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    age=models.IntegerField(max_length=30)
    gender=models.CharField(max_length=30)
    addresss=models.TextField(max_length=300)
    
    #table name
    class Meta:
        db_table='emp'
        
from django import forms

class EmpForm(forms.ModelForm):
    class Meta:
        Model=Emp
        field='__all__'
