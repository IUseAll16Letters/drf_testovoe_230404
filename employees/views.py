from django.db.models import Case, When, Q, F, Count, Sum, Value as V
from django.db.models.functions import Concat
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import EmployeeSerializer, DepartmentSerializer
from .models import Employee, Department


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.select_related('dept').prefetch_related('dept')\
        .only('id', 'name_first', 'name_second', 'name_middle', 'photo',
              'age', 'position', 'salary', 'dept_id', 'dept__name')
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
    filterset_fields = ['name_second', 'dept_id']


class DepartmentViewSet(ModelViewSet):
    pagination_class = None
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Department.objects.select_related('head')\
        .annotate(total_employees=Count('employee__id'),
                  employees_fund=Sum('employee__salary'),
                  head_fullname=Case(
                      When(head__isnull=True, then=None),
                      default=Concat(
                          F('head__name_first'), V(' '),  F('head__name_second'), V(' '), F('head__name_middle')),
                  )
                  )\
        .only('head__name_first', 'head__name_second', 'head__name_middle', 'name', 'id')
