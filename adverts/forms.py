from django.forms import ModelForm

from adverts.models import Advert


class AdvertCreateForm(ModelForm):
    class Meta:
        model = Advert
        fields = ['name', 'author', 'category', 'description', 'price', 'image']
