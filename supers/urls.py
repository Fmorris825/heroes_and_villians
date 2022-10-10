from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.create_super),
    path('<int:pk>/', views.get_super_by_id),
    path('super_types/', include('super_types.urls'))
]