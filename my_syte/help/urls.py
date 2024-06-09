from django.urls import path
from .views import *

urlpatterns = [

    path('userprofile/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile-list'),
    path('userprofile/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),

    path('doctor/', DoctorViewSet.as_view({'get': 'list', 'post': 'create'}), name='doctor-list'),
    path('doctor/<int:pk>/', DoctorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='doctor-detail'),
]
