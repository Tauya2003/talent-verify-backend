from rest_framework.exceptions import ValidationError
from rest_framework.generics import  CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import *
from .serializers import *

# CompanyList, CompanyCreate, CompanyDetail

class CompanyList(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyCreate(CreateAPIView):
    serializer_class = CompanySerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': e.detail})


class CompanyDetail(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



# DepartmentList, DepartmentCreate, DepartmentDetail

class DepartmentList(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentCreate(CreateAPIView):
    serializer_class = DepartmentSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': e.detail})


class DepartmentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer



# RoleList, RoleCreate, RoleDetail

class RoleList(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleCreate(CreateAPIView):
    serializer_class = RoleSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': e.detail})
        

class RoleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer



# EmployeeList, EmployeeCreate, EmployeeDetail

class EmployeeList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeCreate(CreateAPIView):
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': e.detail})
        
    
class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
class FileUpload(CreateAPIView): 
    serializer_class = FileUploadSerializer
    
    def perform_create(self, serializer):
        file = self.request.FILES['file']
        serializer.save(file_path=file)
