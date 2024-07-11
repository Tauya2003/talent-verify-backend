from rest_framework.exceptions import ValidationError
from rest_framework.generics import  CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
import pandas as pd

from django.http import HttpResponse
from django.conf import settings
import os


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
 
                       
class FileUpload(APIView):
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        try:
            data = request.FILES
            serializer = self.serializer_class(data=data)
            if not serializer.is_valid():
                return Response({
                    "status": False,
                    "message": "Invalid file",
                }, status=status.HTTP_400_BAD_REQUEST)
            file = data.get('file')
            file_extension =  file.name.split('.')[-1].lower()
            
            if file_extension == 'xlsx':
                df = pd.read_excel(file, sheet_name=0)
            elif file_extension == 'csv':
                df = pd.read_csv(file)
            else:
                return Response({
                    "status": False,
                    "message": "Unsupported file format",
                }, status=status.HTTP_400_BAD_REQUEST)
                
            employees = []
            for index, row in df.iterrows():
                name = row['Name']
                employee_id = row['Employee ID']
                department = row['Department']
                company = row['Company']
                employee, created = Employee.objects.get_or_create(
                    employee_id=employee_id,
                    defaults={
                        'name': name,
                        'department': Department.objects.get(name=department),
                        'company': Company.objects.get(name=company)
                    }
                )
                if not created:
                    employee.name = name
                    employee.department = Department.objects.get(name=department)
                    employee.company = Company.objects.get(name=company)
                    employee.save()
            return Response({
                "status": True,
                "message": "Employees updated successfully",
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "status": False,
                "message": str(e),
            }, status=status.HTTP_400_BAD_REQUEST)            
            
            
            
# Download Sample files
            
def download_sample_excel(request):
    file_path = os.path.join(settings.BASE_DIR, settings.SAMPLE_EXCEL_FILE)
    with open(file_path, 'rb') as file:
        response = HttpResponse(file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="sample.xlsx"'
        return response

def download_sample_csv(request):
    file_path = os.path.join(settings.BASE_DIR, settings.SAMPLE_CSV_FILE)
    with open(file_path, 'r') as file:
        response = HttpResponse(file, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="sample.csv"'
        return response