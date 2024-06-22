from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    registration_date = models.DateField()
    registartion_number = models.CharField(max_length=20)
    address = models.TextField()
    contact_person = models.CharField(max_length=100)
    related_departments = models.ManyToManyField('Department', related_name='companies')
    num_employees = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name 
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')
    head = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    duties = models.TextField()

    def __str__(self):
        return self.name