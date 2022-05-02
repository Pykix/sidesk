from unicodedata import category

import django_filters

from .models import Category, Project


def categories(request):
    if request is None:
        return Category.objects.none()
    return Category.objects.all()



class MyRangeWidget(django_filters.widgets.RangeWidget):
    
    def __init__(self, min_attrs=None, max_attrs=None, attrs=None):
        super(MyRangeWidget, self).__init__(attrs)
        if min_attrs:
            self.widgets[0].attrs.update(min_attrs)
        if max_attrs:
            self.widgets[1].attrs.update(max_attrs)

class ProjectFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter(label='Prix', widget=MyRangeWidget(min_attrs={'placeholder': 'min',}, max_attrs={'placeholder': "max"}))
    
    category__label = django_filters.ModelChoiceFilter(queryset=categories)
    name = django_filters.CharFilter(lookup_expr='icontains', label="Nom du projet")
    class Meta:
        model = Project
        fields = ['name','category__label']
