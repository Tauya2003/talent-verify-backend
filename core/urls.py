from django.urls import path
from .import views

urlpatterns = [
    # companies routes
    path('companies/', views.CompanyList.as_view(), name='company-view-list'),
    path('companies/new/', views.CompanyCreate.as_view(), name='company-create'),
    path('companies/<int:pk>/', views.CompanyDetail.as_view(), name='company-detail'),

    # departments routes
    path('departments/', views.DepartmentList.as_view(), name='department-view-list'),
    path('departments/new/', views.DepartmentCreate.as_view(), name='department-create'),
    path('departments/<int:pk>/', views.DepartmentDetail.as_view(), name='department-detail'),

    # roles routes
    path('roles/', views.RoleList.as_view(), name='role-view-list'),
    path('roles/new/', views.RoleCreate.as_view(), name='role-create'),
    path('roles/<int:pk>/', views.RoleDetail.as_view(), name='role-detail'),

    # employees routes
    path('employees/', views.EmployeeList.as_view(), name='employee-view-list'),
    path('employees/new/', views.EmployeeCreate.as_view(), name='employee-create'),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view(), name='employee-detail'),
]