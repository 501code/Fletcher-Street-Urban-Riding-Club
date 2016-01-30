from django.contrib import admin
from .models import Page

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Details', {'fields': ['body', 'pub_date']})
    ]
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title', 'body']


admin.site.register(Page, PageAdmin)