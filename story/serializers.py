from rest_framework import serializers 
from story.models import Story, Comment
from user_engine.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id','username']
        read_only_fields = fields

class ReadStorySerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Story 
        fields = ['id','title','url','text','created_at','author']


class WriteStorySerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Story 
        fields = ['id','title','url','text','created_at','author']


class WriteCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','story','comment','user','created_at']


class ReadCommentSerializer(serializers.ModelSerializer):
    story = ReadStorySerializer()
    user = UserSerializer()
    class Meta:
        
        model = Comment
        fields = ['id','story','comment','user','created_at']
        read_only_fields  = fields