from story.models import Story
from story.serializers import  ReadStorySerializer, WriteStorySerializer
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class DashboardViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Story.objects.filter(author=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadStorySerializer 
        return WriteStorySerializer 