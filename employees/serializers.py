from rest_framework import serializers

from .models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'name_first', 'name_second', 'name_middle', 'photo',
                  'age', 'position', 'salary', 'dept']


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    head_fullname = serializers.CharField(default=None, read_only=True)
    total_employees = serializers.DecimalField(decimal_places=2, max_digits=11, read_only=True)
    employees_fund = serializers.DecimalField(decimal_places=2, max_digits=11, read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'name', 'head', 'head_fullname', 'total_employees', 'employees_fund']
