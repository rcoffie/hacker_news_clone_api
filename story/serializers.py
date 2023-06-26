from rest_framework import serializers 
from story.models import Story, Comment


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story 
        fields = ['id','title','url','text','created_at','author']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','story','comment','user','created_at']