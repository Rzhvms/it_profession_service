from django.urls import path

from . import views

app_name = 'form_app'

urlpatterns = [
    path('', views.survey_view, name='form'),
]