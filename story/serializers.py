from rest_framework import serializers 
from story.models import Story, Comment


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story 
        fields = ['id','title','url','text','created_at','author']


class WriteCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','story','comment','user','created_at']


class ReadCommentSerializer(serializers.ModelSerializer):
    story = StorySerializer()
    class Meta:
        
        model = Comment
        fields = ['id','story','comment','user','created_at']
        read_only_fields  = fields