from rest_framework import routers 
from dashboard.views import DashboardViewSet 

router = routers.DefaultRouter()
router.register(r'dashboard_api', DashboardViewSet, basename='task-lists')

urlpatterns = router.urls