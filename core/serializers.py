from rest_framework import serializers
from .models import *
import datetime


class DepartmentSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(slug_field='name', queryset=Company.objects.all())
    class Meta:
        model = Department
        fields = ['name','company']


class RoleSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(required=False)
    
    class Meta:
        model = Role
        fields = ['id','name','employee', 'duties','current','start_date', 'end_date']


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(slug_field='name', queryset=Department.objects.all())
    company = serializers.SlugRelatedField(slug_field='name', queryset=Company.objects.all())
    roles = RoleSerializer(many=True)
    
    # check if the employee id is unique
    def validate_employee_id(self, value):
        if Employee.objects.filter(employee_id=value).exists():
            raise serializers.ValidationError("Employee ID already exists")
        return value

    def create(self, validated_data):
        roles_data = validated_data.pop('roles')
        employee = Employee.objects.create(**validated_data)
        print(roles_data)
        for role_data in roles_data:
            role_data['employee'] = employee
            Role.objects.create(**role_data) 
        return employee
    
    def update(self, instance, validated_data):
        roles_data = validated_data.pop('roles')
        roles = (instance.roles).all()
        roles = list(roles)
        instance.name = validated_data.get('name', instance.name)
        instance.employee_id = validated_data.get('employee_id', instance.employee_id)
        instance.department = validated_data.get('department', instance.department)
        instance.save()

        for role_data in roles_data:
            role = roles.pop(0)
            role.name = role_data.get('name', role.name)
            role.duties = role_data.get('duties', role.duties)
            role.start_date = role_data.get('start_date', role.start_date)
            role.end_date = role_data.get('end_date', role.end_date)
            role.save()
        return instance

    class Meta:
        model = Employee
        fields = ['id','name', 'employee_id', 'company','department','status', 'roles']

        


class CompanySerializer(serializers.ModelSerializer):
    departments = serializers.SerializerMethodField()
    num_employees = serializers.SerializerMethodField(read_only=True)

    def validate(self, data):
        if data['registration_date'] > datetime.date.today():
            raise serializers.ValidationError("Registration date must be in the past")
        return data
    
    def create(self, validated_data):
        return Company.objects.create(**validated_data)
    
    def get_departments(self, instance):
        return DepartmentSerializer(instance.departments, many=True).data
    
    def get_num_employees(self, instance):
        return EmployeeSerializer(instance.employees.all(), many=True).data.__len__()


    class Meta:
        model = Company
        fields = [
            'name',
            'registration_date', 
            'registartion_number',
            'address', 'contact_person', 
            'departments',
            "num_employees", 
            'phone', 
            'email'
            ]

        
