from django.contrib.auth.forms import UserCreationForm
from account.models import User
from django.forms import TextInput, PasswordInput, forms, CharField, EmailField, EmailInput


class RegisterForm(UserCreationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-control'})),
    email = EmailField(label='Почта', widget=EmailInput(attrs={'class': 'form-control'})),
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'})),
    password2 = CharField(label='Повтор пароля', widget=PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'})),

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
