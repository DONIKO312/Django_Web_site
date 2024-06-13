from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#http://127.0.0.1:8000
