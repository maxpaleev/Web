from django.views.generic import UpdateView
from django.views.generic.list import ListView

from account.models import User
from account.forms import ChangeForm, RegisterForm
from django.shortcuts import render, redirect


# импорт модели Artists

def home(request):
    inf = User.objects.filter(id=request.user.id)
    return render(request, 'profile/home.html', {'inf': inf})


class ChangeProfile(UpdateView):
    model = User
    template_name = 'profile/change.html'
    form_class = RegisterForm


# def create(request):
#     error = ''
#     if request.method == 'POST':
#         p = ChangeForm(request.POST)
#         if p.is_valid():
#             p.save()
#             return redirect('/')
#         else:
#             error = 'Форма была неверной'
#
#     p = ChangeForm()
#
#     data = {
#         'p': p,
#         'error': error
#     }
#
#     return render(request, 'profile/change.html', data)
