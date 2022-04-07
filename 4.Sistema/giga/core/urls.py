from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/self-change-password/', views.self_change_password, name='self_change_password'),
]
