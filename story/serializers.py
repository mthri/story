from rest_framework import serializers

from .models import Tag, Story


class GeneralStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'title', 'text', 'preview', 'url',
                  'created_at', 'tags')
        read_only_fields = ('id', 'created_at')
        extra_kwargs = {
            'text': {'write_only': True},
            'url': {'read_only': True},
        }


class DetailsStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'title', 'preview', 'text', 'created_at', 'tags')
        read_only_fields = ('id', 'created_at')


class GeneralTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')