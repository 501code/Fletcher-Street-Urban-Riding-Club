from django.contrib import admin
from .models import Page, Section

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'published', 'section']}),
        ('Details', {'fields': ['body', 'pub_date']})
    ]
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title', 'body']

admin.site.register(Page, PageAdmin)


class SectionAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'visible']
    list_display = ['title', 'description', 'visible']

    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        # Disable delete
        actions = super(SectionAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False
admin.site.register(Section, SectionAdmin)