from django.contrib import admin

from .models import Category, Project


class CategoryInline(admin.TabularInline):
    model = Project.category.through


class CustomProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'get_categories',)
    list_filter = ('name', 'price', 'category',)
    filter_horizontal = ('category',)
    search_fields = ('category__label', 'name',)
    prepopulated_fields = {'slug': ("name",)}

    @admin.display(description="Category")
    def get_categories(self, obj):
        return " | ".join([p.abbreviated for p in obj.category.all()])


admin.site.register(Category)
admin.site.register(Project, CustomProjectAdmin)
