from django.contrib import admin
from .models import Company, Employee, Department

admin.site.site_header = 'Talent Verify Admin'
admin.site.site_title = 'Talent Verify Admin Area'
admin.site.index_title = 'Welcome to the Talent Verify admin area'   
    

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Department)
