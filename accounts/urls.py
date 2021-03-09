from django.urls import path, include
from . import views

user_patterns = ([
    path('<int:id>/', views.users_list, name='detail'),
    path('', views.users_list, name='list'),
], 'users')

urlpatterns = [
    path('users/', include(user_patterns)),
]
