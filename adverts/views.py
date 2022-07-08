from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView

from adverts.forms import AdvertCreateForm, AdvertFilter
from adverts.models import Advert


class AdvertsView(ListView):
    model = Advert
    template_name = 'adverts_list.html'
    paginate_by = 10

    def get_filter(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        filter_ = AdvertFilter(self.request.GET, queryset=queryset)
        return filter_

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_ = AdvertFilter(self.request.GET, queryset)
        return filter_.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter()
        return context


class SingleAdvertView(DetailView):
    model = Advert
    pk_url_kwarg = 'id'
    template_name = 'advert.html'


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
