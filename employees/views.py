from django.db.models import Case, When, Q, F, Value as V, Count, Sum
from django.db.models.functions import Concat
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import EmployeeSerializer, DepartmentSerializer
from .models import Employee, Department


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.select_related('dept').only('id', 'name_first', 'name_second', 'name_middle',
                                                            'age', 'salary', 'dept', 'position', 'dept__name')
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
    filterset_fields = ['name_second', 'dept_id']

    def get_queryset(self):
        if self.request.GET:
            dept_id = self.request.GET.get('dept_id')
            dept_f = Q()
            print(dept_f)
            dept_f = dept_f | Q(dept_id=dept_id)
            print(dept_f)
            print(dept_f & Q())

            print(dept_id)
        ret = super().get_queryset()

        print(ret.query.__str__())
        print(ret)
        return ret


class DepartmentViewSet(ModelViewSet):
    pagination_class = None
    serializer_class = DepartmentSerializer
    queryset = Department.objects.select_related('head')\
        .annotate(total_employees=Count('employee__id', distinct=True),
                  employees_fund=Sum('employee__salary'),
                  head_fullname=Concat(
                      F('head__name_first'), V(' '),  F('head__name_second'), V(' '), F('head__name_middle'))
                  )\
        .only('head__name_first', 'head__name_second', 'head__name_middle', 'name', 'id')
    permission_classes = [IsAuthenticatedOrReadOnly]
