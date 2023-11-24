from rest_framework import serializers
from .models import Phrase, Category, Favorite, Playlist
from django.contrib.auth.models import User
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PhraseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Phrase
        fields = ['id', 'audio_file', 'category',
                  'caption_en', 'caption_pt', 'created_at']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('username', 'password')


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'cover_image']

class FavoriteSerializer(serializers.ModelSerializer):
    playlist = PlaylistSerializer(read_only=True)
    
    class Meta:
        model = Favorite
        fields = ['id', 'playlist']
