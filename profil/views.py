from django.views.generic.list import ListView

from account.models import User
from django.shortcuts import render


# импорт модели Artists

def home(request):
    inf = User.objects.filter(id = request.user.id)
    return render(request, 'profile/home.html', {'inf': inf})