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

# class ListComment(generics.ListAPIView):
#     queryset = Comment.objects.select_related("story","user")
#     serializer_class = ReadCommentSerializer


class ListComment(APIView):
    def get(self, request, format=None):
        comments = Comment.objects.select_related("story","user")
        serializer = ReadCommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WriteCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404 
    
    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = ReadCommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = ReadCommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ListPostComment(generics.ListAPIView):
    serializer_class = ReadCommentSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(story=pk)

class CreateComment(generics.CreateAPIView):
    serializer_class = WriteCommentSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        story = Story.objects.get(pk=pk)
        serializer.save(story=story)


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.select_related("story","user")
    
#     def get_serializer_class(self):
#         if self.action in ("list","retrieve"):
#             return ReadCommentSerializer
#         return WriteCommentSerializer