from django.contrib import admin
from .models import Contactus

# Register your models here.


class ContactusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'email', 'subject', 'name')
    list_filter = ('email', 'subject', 'name')


admin.site.register(Contactus, ContactusAdmin)
