from django.urls import path

from adverts.views import AdvertsView, CreateAdvertView

app_name = 'adverts'

urlpatterns = [
    path('', AdvertsView.as_view(), name='adverts_list'),
    path('create/', CreateAdvertView.as_view(), name='create_advert'),
    ]
