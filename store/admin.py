from django.contrib import admin
from .models import Storedb, Accountdb, Queuedb


# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['storenum']}),
        ('Name',        {'fields': ['storename']}),
        ('Catagory',    {'fields': ['category']}),
        ('Latitude',    {'fields': ['latitude']}),
        ('Longitude',   {'fields': ['longitude']}),
        ('Intro',       {'fields': ['intro']}),
        ('Menu',        {'fields': ['menu']}),
        ('Inform',      {'fields': ['inform']}),
        ('latencytime', {'fields': ['latencytime']})
    ]

    list_display = ['storenum', 'storename', 'category', 'intro', 'menu', 'inform', 'latencytime']
    list_filter = ['category']
    search_fields = ['storenum','storename']
    ordering = ('storenum',)


class StoreManager(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['storenum']}),
        ('ID',          {'fields': ['storeid']}),
        ('PWD',         {'fields': ['storepwd']})
    ]

    list_display = ['storenum', 'storeid', 'storepwd']
    ordering = ('storenum',)


class QueueAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['barcode']}),
        ('OnOff',       {'fields': ['onoffline']}),
        ('storenum',    {'fields': ['storenum']}),
        ('CreateTime',  {'fields': ['createtime']}),
        ('UpdateTime',  {'fields': ['updatetime']}),
        ('status',      {'fields': ['status']})
    ]

    list_display = ['barcode', 'onoffline', 'storenum', 'createtime', 'updatetime', 'status']
    list_filter = ['storenum']
    ordering = ('createtime',)


admin.site.register(Storedb, StoreAdmin)
admin.site.register(Accountdb, StoreManager)
admin.site.register(Queuedb, QueueAdmin)