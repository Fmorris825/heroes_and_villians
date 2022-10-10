from django.urls import path
from . import views

urlpatterns = [
    # path('', views.),
    path('<int:pk>/', views.super_type_list),
]