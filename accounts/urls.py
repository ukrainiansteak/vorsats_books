from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from accounts.views import AccountRegister, AccountLogin, AccountEdit, ChangePasswordView

app_name = 'accounts'

urlpatterns = [
    path('register', AccountRegister.as_view(), name='register'),
    path('login', AccountLogin.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('accounts:login')),
         name='logout'),
    path('', AccountEdit.as_view(), name='edit_profile'),
    path('password', ChangePasswordView.as_view(), name='change_password'),
    ]
