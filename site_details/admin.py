from django.contrib import admin

from .models import SiteDetail


class SiteDetailAdmin(admin.ModelAdmin):
    fields = ['label', 'value']
    list_display = ['label', 'value']
    readonly_fields = ['label']

admin.site.register(SiteDetail, SiteDetailAdmin)
