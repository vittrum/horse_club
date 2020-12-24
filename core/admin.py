from django.contrib import admin
from .models import Schedule, ClientSubscriptions, Discipline, Plan, Subscription

# Register your models here.

admin.site.register(Schedule)
admin.site.register(Discipline)
admin.site.register(Plan)
admin.site.register(ClientSubscriptions)
admin.site.register(Subscription)