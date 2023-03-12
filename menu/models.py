from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserData(models.Model):
    name = models.CharField(max_length=200)
    phone_number = PhoneNumberField(unique=True)


class Category(models.Model):
    title = models.CharField(max_length=250)
    title_ky = models.CharField(max_length=200, blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)


class Extra(models.Model):
    title = models.CharField(max_length=200)
    title_ky = models.CharField(max_length=200, blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField()
    slug = models.SlugField(unique=True)


class Food(models.Model):
    title = models.CharField(max_length=200)
    title_ky = models.CharField(max_length=200, blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    ingredients = models.CharField(max_length=200)
    img = models.ImageField(upload_to='static/img')
    price = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category', blank=True, null=True)
    extras = models.ForeignKey('Extra', on_delete=models.CASCADE, related_name='extras', blank=True, null=True)
