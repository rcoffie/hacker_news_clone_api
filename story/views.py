from story.models import Story, Comment
from story.serializers import ReadCommentSerializer, WriteCommentSerializer, ReadStorySerializer, WriteStorySerializer
from django.http import Http404
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status 
from rest_framework import viewsets
# Create your views here.


class ListStory(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = ReadStorySerializer

class StoryDetail(generics.RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = ReadStorySerializer




class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("story","user")
    
    def get_serializer_class(self):
        if self.action in ("list","retrieve"):
            return ReadCommentSerializer
        return WriteCommentSerializer