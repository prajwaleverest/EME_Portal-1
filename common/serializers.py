from django.db.models import fields
from rest_framework import serializers
from common.models import Departments,Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields =('DepartmentId','DepartmentName')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields =('EmployeeId',
                 'EmployeeName',
                 'Department',
                 'DateOfJoining',
                 'PhotoFileName')