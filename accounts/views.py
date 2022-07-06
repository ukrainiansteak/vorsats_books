from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from accounts.forms import AccountRegisterForm, UserEditForm
from accounts.models import Profile

user = get_user_model()


class AccountRegister(CreateView):
    model = Profile
    template_name = 'register.html'
    success_url = reverse_lazy('index')
    form_class = AccountRegisterForm

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request,
            'Профіль успішно створено.'
        )
        return result


class AccountLogin(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request,
            f'Користувач {self.request.user.first_name} успішно увійшов.'
        )
        return result


class AccountEdit(UpdateView):

    def get(self, request, *args, **kwargs):
        user = request.user
        user_form = UserEditForm(instance=user)

        return render(request, 'profile.html', context={'form': user_form})

    def post(self, request, *args, **kwargs):
        user = request.user
        user_form = UserEditForm(
            instance=user,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Профіль успішно змінено.')
            return redirect(reverse('accounts:edit_profile'))

        return render(request, 'profile.html', context={'form': user_form})


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('accounts:edit_profile')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, 'Пароль успішно змінено.')
        return result
