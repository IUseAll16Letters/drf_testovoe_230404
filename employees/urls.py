from rest_framework.routers import DefaultRouter

from .views import EmployeeViewSet, DepartmentViewSet

router = DefaultRouter()
router.register('employee', EmployeeViewSet, basename='employee')
router.register('department', DepartmentViewSet, basename='department')

urlpatterns = router.urls
