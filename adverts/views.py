from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView

from adverts.forms import AdvertCreateForm
from adverts.models import Advert


class AdvertsView(ListView):
    model = Advert
    template_name = 'adverts.html'


class CreateAdvertView(CreateView):
    model = Advert
    form_class = AdvertCreateForm
    template_name = 'create_advert.html'
    success_url = reverse_lazy('adverts:adverts_list')

    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.get_form()
        if form.is_valid():
            advert = form.save(commit=False)
            advert.seller = user
            advert.save()
            messages.success(request, 'Оголошення успішно створено.')
            return redirect(reverse('adverts:adverts_list'))
        return HttpResponse(status=400)
