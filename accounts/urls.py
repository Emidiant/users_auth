from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UsersList.as_view(), name='users_list'),
    path('users/<int:id>/', views.UsersDetail.as_view(), name='users_detail')
]
