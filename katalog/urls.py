from django.urls import path
from .views import image_upload_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('upload/', image_upload_view, name="images_add"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
