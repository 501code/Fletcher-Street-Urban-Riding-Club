from django.contrib import admin

from .models import SiteDetail


class SiteDetailAdmin(admin.ModelAdmin):
    fields = ['label', 'value']
    list_display = ['label', 'value']
    readonly_fields = ['label']

    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        #Disable delete
        actions = super(SiteDetailAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        #Disable delete
        return False

admin.site.register(SiteDetail, SiteDetailAdmin)
