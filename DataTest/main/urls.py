from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_view, name='data'),
    path('test/', views.test_view, name='test'),
]
