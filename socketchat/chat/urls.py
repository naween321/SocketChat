from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add-user/', views.add_user, name='add_user'),
]