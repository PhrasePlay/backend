from rest_framework import serializers
from .models import Phrase, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PhraseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Phrase
        fields = ['id', 'audio_file', 'category', 'caption_en', 'caption_pt', 'created_at']
