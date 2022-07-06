from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy


class AccountRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("first_name", "last_name", "email")


class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "image")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = password.help_text.replace(
                '../password/', kwargs.pop(reverse_lazy(
                    'accounts:change_password'), './password')
            )
