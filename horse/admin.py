from django.contrib import admin
from .models import Stable, Horse, Photo, StableOccupancy

# Register your models here.

admin.site.register(Stable)
admin.site.register(Photo)
admin.site.register(Horse)
admin.site.register(StableOccupancy)