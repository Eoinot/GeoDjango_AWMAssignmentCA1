from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin
from .models import GolfCourse, Profile

admin.site.register(Profile)
admin.site.register(GolfCourse, admin.OSMGeoAdmin)
