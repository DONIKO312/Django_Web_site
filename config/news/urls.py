from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create/', views.create, name='create'),
    path('list/', views.news_list, name='news_list'),
    path('<int:pk>/', views.news_detail, name='news_detail'),
    path('edit/<int:pk>/', views.news_update, name='news_update'),
    path('delete/<int:pk>/', views.news_delete, name='news_delete'),
    path('create/', views.news_create, name='news_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

