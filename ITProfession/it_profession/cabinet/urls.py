from django.urls import path
from .views import cabinet_view, register_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', cabinet_view, name='cabinet'),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='cabinet/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
]