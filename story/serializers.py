from rest_framework import serializers 
from story.models import Story 


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story 
        fields = ['id','title','url','text','created_at','author']