from django.urls import path
from story.views import DashboardViewSet, ListStory, StoryDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stories', DashboardViewSet, basename='story')
urlpatterns = router.urls

urlpatterns = [
   path('',ListStory.as_view()),
   path('<int:pk>/story_detail/',StoryDetail.as_view()),
]
