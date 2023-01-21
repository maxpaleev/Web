from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = "registration/sign_up.html"
