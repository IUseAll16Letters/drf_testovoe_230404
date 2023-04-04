from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from employees.models import Employee, Department


class TestEmployerSerializer(APITestCase):
    def setUp(self) -> None:
        self.user_1 = User.objects.create(
            username='test_admin_1', email='test@admin.ru', is_staff=True, is_superuser=True
        )
        self.dept_1 = Department.objects.create(name='test_dept_1')
        self.empl_1 = Employee.objects.create(name_first='test_name_1', name_second='test_surname_1',
                                              name_middle='test_middle_1', salary=15000.00, dept_id=1, position=1)
        self.empl_2 = Employee.objects.create(name_first='test_name_2', name_second='test_surname_2',
                                              name_middle='test_middle_2', salary=15000.00, dept_id=1, position=2)

    def test_employee_serializer(self):
        pass
