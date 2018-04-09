from django.urls import path

from . import views

app_name = 'boards'
urlpatterns = [
    # ex: /boards/
    path('', views.home, name='home'),
    
]