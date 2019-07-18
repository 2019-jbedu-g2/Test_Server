from django.contrib import admin
from store.models import Storedb


# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields':['storenum']}),
        ('Name',    {'fields':['storename']}),
        ('Catagory',    {'fields':['category']}),
        ('address',     {'fields':['address']}),
        ('phone',       {'fields':['phonenum']}),
        ('openclose',   {'fields':['openclose']}),
        ('latencytime', {'fields':['latencytime']}),
    ]

    list_display = ['storenum','storename','category','address','phonenum','openclose','latencytime']
    list_filter = ['category']
    search_fields = ['storenum','storename','phonenum']
    ordering = ('storenum',)


admin.site.register(Storedb, StoreAdmin)