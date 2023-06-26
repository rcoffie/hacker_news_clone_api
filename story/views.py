from story.models import Story, Comment
from story.serializers import StorySerializer, CommentSerializer
from django.http import Http404
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import viewsets
# Create your views here.

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer