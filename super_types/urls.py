from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_super_types),
    path('<int:pk>/', views.super_type_list),
]
