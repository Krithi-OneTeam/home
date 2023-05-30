from django.db import models
# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=220)
    ename=models.CharField(max_length=220)
    eemail=models.EmailField()
    econtact=models.CharField(max_length=220)
    class Meta:
        db_table="employee"

