from django.contrib import admin
from .models import *


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'date_created', 'is_draft','slug')
    list_filter = ('title',)
    ordering = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 10


admin.site.register(Blog, BlogAdmin)
