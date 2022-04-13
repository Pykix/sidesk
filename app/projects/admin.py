from django.contrib import admin

from .models import Category, Project, ProjectImage


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',)
    list_filter = ('name', 'price', 'category',)
    search_fields = ('category', 'name',)
    prepopulated_fields = {'slug': ("name",)}

class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('project', 'image')
    search_fields = ('project__name',)

admin.site.register(ProjectImage, ProjectFileAdmin)
admin.site.register(Category)
admin.site.register(Project, ProjectAdmin)
