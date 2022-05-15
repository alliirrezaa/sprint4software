from django.contrib import admin
from .models import *

class CartAdmin(admin.ModelAdmin):
    list_display=['user','form']

admin.site.register(Cart,CartAdmin)
