from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    registration_date = models.DateField()
    registartion_number = models.CharField(max_length=20)
    address = models.TextField()
    contact_person = models.CharField(max_length=100)
    # departments = models.ManyToManyField('Department', related_name='companies')
    num_employees = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name