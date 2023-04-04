from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from rest_framework.routers import DefaultRouter
from employees.views import EmployeeViewSet, DepartmentViewSet


router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employees')
router.register('departments', DepartmentViewSet, basename='departments')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)