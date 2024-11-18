from django.contrib import admin

from .models import Order, CustomUser

admin.site.register(Order)
admin.site.register(CustomUser)