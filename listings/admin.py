from django.contrib import admin
from listings.models import *



class SaleAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'email', 'user', 'category', 'area', 'date_created', 'active')


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'gate_fee', 'email', 'user', 'category', 'area', 'start_date', 'end_date', 'date_created', 'active')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'email', 'user', 'category', 'area', 'date_created', 'active')


class HousingAdmin(admin.ModelAdmin):
    list_display = ('title', 'condition', 'duration', 'price', 'email', 'user', 'category', 'area', 'date_created', 'active')


class CommunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'duration', 'email', 'user', 'category', 'area', 'date_created', 'active')


admin.site.register(Sale, SaleAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Housing, HousingAdmin)
admin.site.register(Community, CommunityAdmin)