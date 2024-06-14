# Import necessary modules
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

# Define URL patterns
urlpatterns = [
    # Home page for news
    path('', views.news_home, name='news_home'),

    # Route for creating news
    path('create/', views.create, name='create'),

    # Route for listing news
    path('list/', views.news_list, name='news_list'),

    # Route for viewing news detail with <int:pk> as a parameter
    path('<int:pk>/', views.news_detail, name='news_detail'),

    # Route for editing news with <int:pk> as a parameter
    path('edit/<int:pk>/', views.news_update, name='news_update'),

    # Route for deleting news with <int:pk> as a parameter
    path('delete/<int:pk>/', views.news_delete, name='news_delete'),

    # Another route for creating news
    path('create/', views.news_create, name='news_create'),
]

# Add static file serving if DEBUG is True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)