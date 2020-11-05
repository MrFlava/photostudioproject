import enum

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# class OrderType(enum.Enum):
#     FILM_DEVELOPMENT = 'film development'
#     PHOTO_PRINTING_AND_DEVELOPMENT = 'Photo printing and development'
#     PRINT_TOGETHER = 'print together'

# class PaperType(enum.Enum):
#     MATTE = 'Matte'
#     GLOSSY = 'Glossy'
#     SEMI_GLOSSY = 'Semi-Glossy'
#     SUPERGLOSSY = 'SuperGlossy'
#     SILK = 'Silk'
#     SATIN = 'Satin'


class PhotoCenter(models.Model):
    title = models.CharField(max_length=120)
    headquarters_address = models.CharField(max_length=250)

    objects = models.Manager()

    def __str__(self):
        return f"{self.title} located at {self.headquarters_address}"


class PhotoOffice(models.Model):
    address = models.CharField(max_length=250)
    workplaces_quantity = models.IntegerField(default=1,
                                              validators=[
                                                  MaxValueValidator(20),
                                                  MinValueValidator(1)
                                              ]
                                              )
    center = models.ForeignKey(PhotoCenter, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f"Office #{self.pk} located at {self.address}"


class PhotoStand(models.Model):
    address = models.CharField(max_length=250)
    workplaces_quantity = models.IntegerField(default=1,
                                              validators=[
                                                  MaxValueValidator(3),
                                                  MinValueValidator(1)
                                              ]
                                              )
    office = models.ForeignKey(PhotoOffice, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f"Stand #{self.pk} located at {self.address}"


# class Order(models.Model):
#
# class Item(models.Model):
#
# class Customer(models.Model):