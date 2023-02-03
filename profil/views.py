from django.views.generic.list import ListView

from account.models import User


# импорт модели Artists

class home(ListView):
    model = User
    template_name = 'profile/home.html'
    context_object_name = 'inf'