from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_disaster, name='home'),
    path('report/', views.report_disaster, name='report_disaster'),
    path('reports/', views.view_reports, name='view_reports'),
    path('predict/', views.predict_disaster, name='predict_disaster'),  # NEW
]
