from django.contrib import admin
from .models import *


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'date_created', 'is_draft')
    list_filter = ('title',)
    ordering = ('title',)
    search_fields = ('title',)


admin.site.register(Blog, BlogAdmin)
