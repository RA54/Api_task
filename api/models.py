from django.db import models

# Create your models here.


class Product(models.Model):
    Employe_name = models.CharField(max_length=200, null=False, blank=False)
    Employe_ID = models.CharField(max_length=100, null=False, blank=False)
    City = models.CharField(max_length=100, null=False, blank=False)
    Email = models.CharField(max_length=100, null=False, blank=False)
    Phone_NO = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.Employe_name

