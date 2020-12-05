import enum
import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model


# Create your models here.


class AdditionalServicesType(enum.Enum):
    PASSPORT_PHOTO = 'Passport photo'
    PHOTO_RESTORATION = 'Photo restoration'
    CAMERA_RENTAL = 'Camera rental'
    ART_PHOTO = 'Art photo'
    PROFESSIONAL_PHOTOGRAPHER = 'Professional photographer'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class ItemType(enum.Enum):
    CAMERA = 'Camera'
    LENSES = 'Lenses'
    OUTBREAKS = 'Outbreaks'
    PHOTO_PAPER = 'Photo paper'
    CAMERA_ROLL = 'Camera roll'
    PHOTOGRAPHIC_REAGENTS = 'Photographic reagents'
    ALBUM = 'Album'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class ProfileType(enum.Enum):
    PROFESSIONAL = 'Professional'
    FAN = 'Fan'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class OrderType(enum.Enum):
    FILM_DEVELOPMENT = 'Film development'
    PHOTO_PRINTING_AND_DEVELOPMENT = 'Photo printing and development'
    PRINT_TOGETHER = 'Print together'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class OrderPriorityType(enum.Enum):
    URGENT_PRIORITY = 'Urgent priority'
    ORDINARY_PRIORITY = 'Ordinary priority'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class PaperFormat(enum.Enum):
    A0 = 'A0'
    A1 = 'A1'
    A2 = 'A2'
    A3 = 'A3'
    A4 = 'A4'
    A5 = 'A5'
    A6 = 'A6'
    A7 = 'A7'
    A8 = 'A8'
    A9 = 'A9'
    A10 = 'A10'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class PaperType(enum.Enum):
    MATTE = 'Matte'
    GLOSSY = 'Glossy'
    SEMI_GLOSSY = 'Semi-Glossy'
    SUPERGLOSSY = 'SuperGlossy'
    SILK = 'Silk'
    SATIN = 'Satin'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


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


class UserProfile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    type = models.CharField(max_length=120, choices=ProfileType.choices())

    objects = models.Manager()

    def __str__(self):
        return f"Profile #{self.pk}: {self.user}"


class Order(models.Model):
    photos_from_each_frame_quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    photos_quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    paper_format = models.CharField(max_length=120, choices=PaperFormat.choices())
    paper_type = models.CharField(max_length=120, choices=PaperType.choices())
    priority = models.CharField(max_length=120, choices=OrderPriorityType.choices())
    order_type = models.CharField(max_length=120, choices=OrderType.choices(), default=OrderType.FILM_DEVELOPMENT)
    creation_date = models.DateTimeField(default=datetime.datetime.now())
    term = models.DateTimeField(default=datetime.datetime.now())
    photo_office = models.ForeignKey(PhotoOffice, on_delete=models.CASCADE, null=True, blank=True)
    photo_stand = models.ForeignKey(PhotoStand, on_delete=models.CASCADE, null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f"Order #{self.pk}for {self.customer}"


class Provider(models.Model):
    name = models.CharField(max_length=120)
    items = models.ManyToManyField('Item', through='ItemProvider')

    objects = models.Manager()

    def __str__(self):
        return f"Provider #{self.pk}: {self.name}"


class Item(models.Model):
    item_type = models.CharField(max_length=120, choices=ItemType.choices())
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=250)
    price = models.PositiveIntegerField(default=0)
    photo_office = models.ForeignKey(PhotoOffice, on_delete=models.CASCADE, null=True, blank=True)
    photo_stand = models.ForeignKey(PhotoStand, on_delete=models.CASCADE, null=True, blank=True)
    providers = models.ManyToManyField('Provider', through='ItemProvider')
    quantity = models.PositiveIntegerField(default=1)

    objects = models.Manager()

    def __str__(self):
        return f"Item #{self.pk}: {self.item_type}, {self.title}"


class ItemProvider(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f"Provider {self.provider}for  {self.item}"


class AdditionalService(models.Model):
    service_type = models.CharField(max_length=120, choices=AdditionalServicesType.choices())
    photo_office = models.ForeignKey(PhotoOffice, on_delete=models.CASCADE)


class ItemOrder(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=datetime.datetime.now())

    objects = models.Manager()

    def __str__(self):
        return f"Order #{self.pk}for  {self.customer}"


class AdditionalServicesOrder(models.Model):
    additional_service = models.ForeignKey(AdditionalService, on_delete=models.CASCADE)
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=datetime.datetime.now())

    objects = models.Manager()

    def __str__(self):
        return f"Order #{self.pk}for  {self.customer}"
