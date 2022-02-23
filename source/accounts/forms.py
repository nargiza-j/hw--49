from django import forms
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm, UsernameField

from accounts.models import Profile

User = get_user_model()


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        if not (first_name or last_name):
            raise forms.ValidationError('Заполните хотя бы одно поле: first_name или last_name!')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']
        field_classes = {'username': UsernameField}


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("avatar", "profile_url", "about_info")



# class MyUserCreationForm(forms.ModelForm):
#     password = forms.CharField(label="Пароль", widget=forms.PasswordInput,
#                                        strip=False)
#     password_confirm = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput,
#                                        strip=False)
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_confirm = cleaned_data.get("password_confirm")
#         if password != password_confirm:
#             raise ValidationError("Пароли не совпадают")
#         return cleaned_data
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data.get("password"))
#         if commit:
#             user.save()
#         return user
#
#     class Meta:
#         model = User
#         fields = ("username", "password", "password_confirm", "email", "first_name", "last_name")