from django.db import models
from datetime import date

from django.contrib.admin.widgets import AdminDateWidget

# Create your models here.


class Travel_reg(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=20)
    
    class Meta:
        db_table="travel_reg"
    def __str__(self):
        return f"{self.username} {self.email}"

class Travel_book(models.Model):
    dest=(
    ("kerala","kerala"),
    ("tamil nadu","tamil nadu"),
    ("karnataka","karnataka"),
    ("up","up"),
    ("mp","mp"),
    ("delhi","delhi"),
    ("ap","ap"),


)
    username=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=254,null=True)
    phone=models.IntegerField(null=True)
    location=models.CharField(max_length=30,choices=dest,default="kerala",null=True)
    destination=models.CharField(max_length=30,choices=dest,default="delhi",null=True)
    # child=models.IntegerField()
    # adult=models.IntegerField()
    num_travelers=models.IntegerField(null=True)
    sdate=models.DateField(null=True)
    edate=models.DateField(null=True)
    
    class Meta:
        db_table="travel_book"
    def __str__(self):
        return f"{self.username} {self.phone} {self.destination}"

class Destination(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='destination_image/')
    def __str__(self):
        return f"{self.name}"