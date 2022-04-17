from django.contrib import admin
from .models import *


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'date_created', 'is_draft')


admin.site.register(Blog,BlogAdmin)
