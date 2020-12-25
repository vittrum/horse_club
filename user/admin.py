from django.contrib import admin
from .models import Role, Owner, UserProfile, User

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Owner)
admin.site.register(Role)
