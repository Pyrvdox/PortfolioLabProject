from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField()


class Institution(models.Model):
    organizations = (
        ('fundacja', 'Fundacja'),
        ('organizacja_pozarzadowa', 'Organizacja Pozarządowa'),
        ('zbiorka_lokalna', 'Zbiórka Lokalna'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=30, choices=organizations, default='fundacja')
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, default=None)

