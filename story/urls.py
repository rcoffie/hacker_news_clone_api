from django.urls import path
from story.views import CommentViewSet,ListStory, StoryDetail
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'comment_api',CommentViewSet, basename="comment")


urlpatterns = [
   path('',ListStory.as_view()),
   path('<int:pk>/story_detail/',StoryDetail.as_view()),
]
urlpatterns = router.urls
