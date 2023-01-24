from django.shortcuts import render

from .forms import UserCreate


def signup(request):
    error = ''
    if request.method == 'POST':
        form = UserCreate(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверной'

    form = UserCreate()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'registration/signup.html', data)
