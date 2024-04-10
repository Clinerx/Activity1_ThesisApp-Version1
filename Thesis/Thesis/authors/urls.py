from django.urls import path
from . import views

urlpatterns = [
    path('', views.thesis_list, name='thesis_list'),
    path('<int:thesis_id>/', views.thesis_detail, name='thesis_detail'),
]