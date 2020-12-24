from django.contrib import admin
from .models import Trainer, Client, Role, Owner

# Register your models here.
admin.site.register(Trainer)
admin.site.register(Client)
admin.site.register(Owner)
admin.site.register(Role)
