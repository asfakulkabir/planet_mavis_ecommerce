# admin.py
from django.contrib import admin
from .models import *
from django.utils.html import format_html
from unfold.admin import ModelAdmin


@admin.register(Banner)
class BannerAdmin(ModelAdmin):
    list_display = ['thumbnail_preview', 'title', 'is_active', 'for_mobile', 'created_at']
    list_filter = ['is_active', 'for_mobile']

    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" style="border-radius: 8px;" />'.format(obj.image.url))
        return "No Image"

    thumbnail_preview.short_description = 'Image'

    
@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ['id', 'image', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']

@admin.register(HomeComponents)
class HomeComponentsAdmin(ModelAdmin):
    list_display = ('title', 'category', 'image_tag')
    list_filter = ('category',)
    search_fields = ('title',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />'.format(obj.image.url))
        return "No Image"

    image_tag.short_description = 'Image'


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',) # Ensure created_at can't be changed after creation
