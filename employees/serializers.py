from rest_framework import serializers

from .models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    dept_name = serializers.CharField(source='dept.name', default=None)

    class Meta:
        model = Employee
        fields = ['id', 'name_first', 'name_second', 'name_middle', 'photo',
                  'age', 'position', 'salary', 'dept_id', 'dept_name']


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    head_fullname = serializers.ReadOnlyField(default=None)
    total_employees = serializers.ReadOnlyField()
    employees_fund = serializers.ReadOnlyField()

    class Meta:
        model = Department
        fields = ['id', 'name', 'head', 'head_fullname', 'total_employees', 'employees_fund']
