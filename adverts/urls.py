from django.urls import path

from adverts.views import AdvertsView, CreateAdvertView, SingleAdvertView

app_name = 'adverts'

urlpatterns = [
    path('', AdvertsView.as_view(), name='adverts_list'),
    path('<int:id>', SingleAdvertView.as_view(), name='advert'),
    path('create/', CreateAdvertView.as_view(), name='create_advert'),
    ]
