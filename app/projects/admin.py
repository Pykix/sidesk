from django.contrib import admin

from .models import Category, Order, Project, ProjectImage, ProjectMetric


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    max_num = 1


class ProjectMetricInline(admin.StackedInline):
    model = ProjectMetric
    max_num = 1


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = (
        "name",
        "price",
        "category",
    )
    list_filter = (
        "name",
        "price",
        "category",
    )
    inlines = [ProjectImageInline, ProjectMetricInline]
    search_fields = (
        "category",
        "name",
    )
    prepopulated_fields = {
        "slug": ("name",),
    }


class ProjectFileAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "image",
    )
    search_fields = ("project__name",)


class ProjectMetricAdmin(admin.ModelAdmin):
    list_display = ("project",)
    search_fields = ("project__name",)


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "bill_number",
        "project",
        "seller",
        "buyer",
    )

    search_fields = (
        "project__name",
        "bill_number",
    )
    exclude = ("bill_number",)


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectFileAdmin)
admin.site.register(ProjectMetric, ProjectMetricAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
