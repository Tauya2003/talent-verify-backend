from django.shortcuts import render
from rest_framework import generics
from .models import Company
from .serializers import CompanySerializer

class CompanyListCreate(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

