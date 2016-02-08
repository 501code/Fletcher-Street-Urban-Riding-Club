from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['subject', 'email']
    readonly_fields = Contact._meta.get_all_field_names()

    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        # Disable delete
        actions = super(ContactAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Contact, ContactAdmin)