from django.urls import path
from story.views import ListStory, StoryDetail, ListComment, CommentDetail, ListPostComment,CreateComment




urlpatterns = [
   path('',ListStory.as_view()),
   path('<int:pk>/story_detail/',StoryDetail.as_view()),
   path('list_comment_api/',ListComment.as_view()),
   path('comment/<int:pk>/',CommentDetail.as_view()),
   path('list_post_comment/<int:pk>/',ListPostComment.as_view()),
   path('create_comment/<int:pk>/',CreateComment.as_view()),


]

