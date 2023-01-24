from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class UserCreate(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'is_superuser', 'is_staff')


class UserChange(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'is_superuser', 'is_staff')
