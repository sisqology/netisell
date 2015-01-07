from django.contrib import admin
from institutions.models import Institution, Area


class AreaInline(admin.TabularInline):
    model = Area
    extra = 3


class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution')


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'abbr')
    inlines = [AreaInline]

admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Area, AreaAdmin)