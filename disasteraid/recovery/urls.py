from django.urls import path
from . import views

urlpatterns = [
    path('', views.recovery_home, name='recovery_home'),
]
