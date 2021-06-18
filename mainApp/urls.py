from django.urls import path

from . import views


urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('category/<int:pk>/', views.FeedList.as_view(), name='category_feeds'),
    path('feed/<int:pk>/articles/', views.ArticleList.as_view(), name='feed_articles'),
]

