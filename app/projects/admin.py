from django.contrib import admin

from .models import Category, Project


class CategoryInline(admin.TabularInline):
    model = Project.category.through


class CustomProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'get_categories',)
    list_filter = ('title', 'price', 'category',)
    filter_horizontal = ('category',)
    search_fields = ('category__label', 'title',)
    prepopulated_fields = {'slug': ("title",)}

    @admin.display(description="Category")
    def get_categories(self, obj):
        return " | ".join([p.get_label_display() for p in obj.category.all()])


admin.site.register(Category)
admin.site.register(Project, CustomProjectAdmin)
