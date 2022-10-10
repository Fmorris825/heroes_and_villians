from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_super),
    path('<int:pk>/', views.get_super_by_id),
]