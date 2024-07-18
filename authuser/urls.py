from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-view-list'),
    path('users/new/', views.UserCreate.as_view(), name='user-create'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
]