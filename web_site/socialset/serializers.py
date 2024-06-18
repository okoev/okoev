from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = 'all'

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = 'all'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 'all'


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = 'all'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Comment
        fields = 'all'

class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model =CommentLike
        fields = 'all'

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Story
        fields = 'all'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = 'all'