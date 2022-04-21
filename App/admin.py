from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django_summernote.admin import SummernoteModelAdmin
from App.resources import BlogResource


# Register your models here.

class BlogAdmin(ImportExportModelAdmin):
    list_display = ('title', 'body', 'date_created', 'is_draft', 'slug')
    list_filter = ('title',)
    ordering = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 10
    actions = ('Cross', 'Tick')
    date_hierarchy = 'date_created'
    fields = ('title','body','is_draft','slug')

    def Cross(self, request, queryset):
        queryset.update(is_draft=False)

    def Tick(self, request, queryset):
        queryset.update(is_draft=True)

    resource_class = BlogResource


admin.site.register(Blog, BlogAdmin)
