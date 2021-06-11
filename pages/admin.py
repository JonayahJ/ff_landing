from pages.models import Expert
from django.contrib import admin
from .models import Expert
from django.utils.html import format_html

# Register your models here.

class ExpertAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px" />'.format(object.headshot.url))
    
    thumbnail.short_description = "Headshot"
    
    list_display = ("id", "thumbnail", "name", "designation", "created_at")
    list_display_links = ("id", "thumbnail", "name")
    search_fields = ("name", "designation")
    list_filter = ("designation",)

admin.site.register(Expert, ExpertAdmin)