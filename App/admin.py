from django.contrib import admin
from .models import *


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
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


admin.site.register(Blog, BlogAdmin)
