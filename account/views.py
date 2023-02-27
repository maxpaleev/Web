from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        image = request.FILES['image']

        context = {'form': form,
                   'username': username,
                   'password1': password1,
                   'password2': password2,
                   'email': email,
                   'image': image}

        if form.is_valid():
            form.save()

            return redirect('/')

    else:
        form = RegisterForm()
        context = {'form': form
                   }

    return render(request, 'registration/signup.html', context)
