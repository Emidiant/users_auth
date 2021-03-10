"""accounts URL Configuration."""
from . import views
from django.urls import path


urlpatterns = [
    path('users/', views.UsersList.as_view(), name='users_list'),
    path('users/<int:id>/', views.UsersDetail.as_view(), name='users_detail'),
]
