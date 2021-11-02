from django.contrib import admin
from .models import FoundItem, LostItem

# Register your models here.

admin.site.register(LostItem)
admin.site.register(FoundItem)