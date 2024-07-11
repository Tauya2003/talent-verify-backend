from django.db import models
from django.contrib.auth import get_user_model

class Company(models.Model):
    name = models.CharField(max_length=100)
    registration_date = models.DateField()
    registration_number = models.CharField(max_length=20)
    address = models.TextField()
    contact_person = models.CharField(max_length=100)
    num_employees = models.IntegerField(default=0)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name 
    
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return self.name
      
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    status = models.BooleanField(default=True)
    

    def __str__(self):
        return self.name
    

class Role(models.Model):
    name = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='roles', null=True, blank=True)
    duties = models.TextField()
    start_date = models.DateField(auto_now_add=True, null=True, blank=True)
    end_date = models.DateField( null=True, blank=True)
    current = models.BooleanField(default=True)

    def __str__(self):
        return self.name
 
    
User = get_user_model()

class UploadedFile(models.Model):
    file_name = models.CharField(max_length=100)
    file_type = models.CharField(max_length=20)
    file_path = models.FilePathField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
  