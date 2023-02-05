from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='profile'),
    path('/<int:pk>/update', views.ChangeProfile.as_view(), name='change')
]
