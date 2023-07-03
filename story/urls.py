from django.urls import path
from story.views import ListStory, StoryDetail, ListComment, CommentDetail





urlpatterns = [
   path('',ListStory.as_view()),
   path('<int:pk>/story_detail/',StoryDetail.as_view()),
   path('list_comment_api/',ListComment.as_view()),
   path('comment/<int:pk>/',CommentDetail.as_view()),
]

