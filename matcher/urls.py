from django.urls import path

from . import views

urlpatterns = [
    path('<int:sock_id>/', views.detail, name='detail'),
    path('add_sock/', views.add_sock, name='add_sock'),
]

