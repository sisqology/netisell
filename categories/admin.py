from django.contrib import admin
from categories.models import *


class SaleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created')
    #inlines = [SubcategoryInline]


class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created')


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created')


class HousingCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created')


class CommunityCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created')


#class DiscussionCategoryAdmin(admin.ModelAdmin):
#    list_display = ('name', 'date_created')


admin.site.register(SaleCategory, SaleCategoryAdmin)
admin.site.register(EventCategory, EventCategoryAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(HousingCategory, HousingCategoryAdmin)
admin.site.register(CommunityCategory, CommunityCategoryAdmin)
#admin.site.register(DiscussionCategory, DiscussionCategoryAdmin)