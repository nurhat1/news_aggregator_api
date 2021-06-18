from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CategorySerializer, FeedSerializer, ArticleSerializer
from .services import parse_feed_articles
from .exceptions import InvalidFeedLink
from .models import Category, Feed

# Create your views here.


class CategoryList(APIView):
    def get(self, request):
        # get active categories
        categories = Category.objects.filter(is_active=True)
        category_serializer = CategorySerializer(categories, many=True)
        return Response({"status": status.HTTP_200_OK, "data": category_serializer.data})


class FeedList(APIView):
    def get(self, request, pk):
        # get feed by category id
        feeds = Feed.objects.filter(category__id=pk)
        feeds_serializer = FeedSerializer(feeds, many=True)
        return Response({"status": status.HTTP_200_OK, "data": feeds_serializer.data})


class ArticleList(APIView):
    def get(self, request, pk):
        try:
            # get feed by id
            feed = Feed.objects.get(id=pk)
            # get feed articles
            articles_data = parse_feed_articles(feed)
        except Feed.DoesNotExist:
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Feed does not exist."})
        except InvalidFeedLink:
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Invalid feed."})
        article_serializer = ArticleSerializer(articles_data, many=True)

        return Response({"status": status.HTTP_200_OK, "data": article_serializer.data})
