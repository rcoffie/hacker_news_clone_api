from django.urls import path
from story.views import StoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stories', StoryViewSet, basename='story')
urlpatterns = router.urls

urlpatterns = [
    
]
