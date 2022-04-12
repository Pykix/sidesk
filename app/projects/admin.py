from django.contrib import admin

from .models import Category, Project


class CustomProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',)
    list_filter = ('name', 'price', 'category',)
    search_fields = ('category', 'name',)
    prepopulated_fields = {'slug': ("name",)}




admin.site.register(Category)
admin.site.register(Project, CustomProjectAdmin)
