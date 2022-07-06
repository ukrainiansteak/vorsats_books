import django_filters
from django.db import models
from django.forms import ModelForm

from adverts.models import Advert


class AdvertCreateForm(ModelForm):
    class Meta:
        model = Advert
        fields = ['name', 'author', 'category', 'description', 'price', 'image']


class AdvertFilter(django_filters.FilterSet):
    class Meta:
        model = Advert
        fields = ['name']

        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }
