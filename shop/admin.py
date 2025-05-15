from django.contrib import admin
from .models import Laptop

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'processor', 'ram_gb', 'storage_gb', 'price', 'stock')
    search_fields = ('brand', 'model', 'processor')
    list_filter = ('brand', 'ram_gb', 'storage_gb')
