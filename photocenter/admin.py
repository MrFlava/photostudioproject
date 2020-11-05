from django.contrib import admin

from .models import PhotoCenter, PhotoOffice, PhotoStand

# Register your models here.


class PhotoCenterAdmin(admin.ModelAdmin):
    model = PhotoCenter


class PhotoOfficeAdmin(admin.ModelAdmin):
    model = PhotoOffice


class PhotoStandAdmin(admin.ModelAdmin):
    model = PhotoStand


admin.site.register(PhotoCenter, PhotoCenterAdmin)
admin.site.register(PhotoOffice, PhotoOfficeAdmin)
admin.site.register(PhotoStand, PhotoStandAdmin)