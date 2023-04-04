from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from employees.models import Employee, Department


class TestEmployerApi(APITestCase):

    def setUp(self) -> None:
        self.user_1 = User.objects.create(
            username='test_admin_1', email='test@admin.ru', is_staff=True, is_superuser=True
        )
        self.empl_url = reverse('employee-list')
        self.dept_url = reverse('department-list')
        self.empl_data = {
            'name_first': 'name_first_test',
            'name_second': 'name_second_test',
            'name_middle': 'name_middle_test',
            'age': 25,
            'salary': 15000,
            'dept': 1,
            'position': 1,
        }

    def test_get_employee_authed(self):
        self.client.force_login(user=self.user_1)
        response = self.client.get(path=self.empl_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee_not_authed(self):
        response = self.client.get(path=self.empl_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_dept_authed(self):
        self.client.force_login(user=self.user_1)
        response = self.client.get(path=self.dept_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_dept_not_authed(self):
        response = self.client.get(path=self.dept_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_employee_authed(self):
        self.client.force_login(user=self.user_1)
        self.dept_1 = Department.objects.create(name='test_dept_1')

        response = self.client.post(path=self.empl_url, data=self.empl_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        employee_query = Employee.objects.values().last()

        employee_query.pop('created')
        employee_query.pop('updated')
        employee_query.update(**{'photo': None, 'salary': str(employee_query['salary'])})
        employee_query.pop('dept_id')
        response.data.pop('dept')
        self.assertEqual(response.data, employee_query)

    def test_create_employee_not_authed(self):
        response = self.client.post(path=self.empl_url, data=self.empl_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_employee_authed(self):
        self.dept_1 = Department.objects.create(name='test_dept_1')
        self.empl_data.update({'dept': self.dept_1})
        self.empl_1 = Employee.objects.create(**self.empl_data)
        employee_data = Employee.objects.values().last()
        employee_data.update({"name_first": 'new_name_first_1', 'dept': 1})
        employee_data.pop('dept_id')
        self.client.force_login(self.user_1)
        empl_url = reverse('employee-detail', args=(self.empl_1.id, ))

        response = self.client.put(path=empl_url, data=employee_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_del_employee_authed(self):
        self.dept_1 = Department.objects.create(name='test_dept_1')
        self.empl_data.update({'dept': self.dept_1})
        self.empl_1 = Employee.objects.create(**self.empl_data)
        self.client.force_login(self.user_1)
        empl_url = reverse('employee-detail', args=(self.empl_1.id,))
        response = self.client.delete(path=empl_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
