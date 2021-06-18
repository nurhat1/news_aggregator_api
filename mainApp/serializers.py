from rest_framework import serializers

from .models import Category, Feed


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class FeedSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Feed
        fields = '__all__'


class ArticleSerializer(serializers.Serializer):
    feed = FeedSerializer(read_only=True)
    title = serializers.CharField(max_length=250)
    link = serializers.URLField()
    summary = serializers.CharField()
    published_str = serializers.CharField()
    published = serializers.DateTimeField()
