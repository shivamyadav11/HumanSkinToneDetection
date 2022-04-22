from django.contrib import admin
from .models import *
# Register your models here.


class Image_uploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_id')
    list_display_links = ('id', 'img_id')


admin.site.register(Image_upload, Image_uploadAdmin)
