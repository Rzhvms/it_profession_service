from django.urls import path

from . import views

app_name = 'community'

urlpatterns = [
    path('about/', views.about_view, name='about'),
    path('faq/', views.faq_view, name='faq'),
]