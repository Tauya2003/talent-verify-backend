from django.urls import path
from .import views

urlpatterns = [
    path('companies/', views.CompanyListCreate.as_view(), name='company-view-create')
]