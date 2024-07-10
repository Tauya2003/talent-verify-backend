import os
import csv
from django.conf import settings
from .models import Company, Department, Employee, Role

def process_csv(uploaded_file):
    file_path = uploaded_file.file_path
    
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            company_name = row['Company Name']
            registration_date = row['Registration Date']
            registration_number = row['Registration Number']
            address = row['Address']
            contact_person = row['Contact Person']
            # departments = row['Departments']
            # num_employees = int(row['Number of Employees'])
            phone = row['Phone']
            email = row['Email']
            
            # employee_name = row['Employee Name']
            # employee_id = row['Employee ID']
            # department = row['Department']
            # role = row['Role']
            # start_date = row['Start Date']
            # end_date = row['End Date']
            # duties = row['Duties']
            
            # Update or create company
            company, created = Company.objects.get_or_create(
                name=company_name,
                defaults={
                    'registration_date': registration_date,
                    'registration_number': registration_number,
                    'address': address,
                    'contact_person': contact_person,
                    # 'departments': departments,
                    # 'num_employees': num_employees,
                    'phone': phone,
                    'email': email
                }
            )
            
            # # Update or create employee
            # employee, created = Employee.objects.get_or_create(
            #     name=employee_name,
            #     company=company,
            #     defaults={
            #         'employee_id': employee_id,
            #         'department': department,
            #         'role': role,
            #         'start_date': start_date,
            #         'end_date': end_date,
            #         'duties': duties
            #     }
            # )
            
            
             # Save the updated company and employee
            company.save()
            # employee.save()
        

def process_text(uploaded_file):
    # Parse the text file
    # Update company and employee data based on the text contents
    pass

def process_excel(uploaded_file):
    # Parse the Excel file
    # Update company and employee data based on the Excel contents
    pass


def save_file(file):
    file_path = os.path.join(settings.MEDIA_ROOT, file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return file_path

def get_file_type(file_name):
    extension = file_name.split('.')[-1].lower()
    if extension == 'csv':
        return 'csv'
    elif extension == 'txt':
        return 'text'
    elif extension in ['xls', 'xlsx']:
        return 'excel'
    else:
        return 'unknown'
    
    
    
def process_file(uploaded_file):
    if uploaded_file.file_type == 'csv':
        process_csv(uploaded_file)
    elif uploaded_file.file_type == 'text':
        process_text(uploaded_file)
    elif uploaded_file.file_type == 'excel':
        process_excel(uploaded_file)
    else:
        raise ValueError("Unknown file type")
    
