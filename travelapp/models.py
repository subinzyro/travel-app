from django.db import models

# Create your models here.

class Travel_reg(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=20)
    
    class Meta:
        db_table="travel_register"
    def __str__(self):
        return f"{self.username} {self.email}"

class Travel_book(models.Model):
    phone=models.IntegerField()
    location=models.CharField(max_length=200)
    destination=models.CharField(max_length=200)
    child=models.IntegerField()
    adult=models.IntegerField()
    sdate=models.DateField()
    edate=models.DateField()

    class Meta:
        db_table="travel_book"
    def __str__(self):
        return f"{self.phone} {self.destination}"

