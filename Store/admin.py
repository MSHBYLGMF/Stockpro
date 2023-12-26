from django.contrib import admin
from .import models
# Register your models here.

from .import forms
class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['category', 'item_name', 'quantity']
   form = forms.StockCreateForm
   list_filter = ['category']
   search_fields = ['category', 'item_name']


admin.site.register(models.Stock,StockCreateAdmin)
