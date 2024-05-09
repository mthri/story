from django.urls import path

from .views import StoryListCreateView, StoryDetailView, TagListCreateView


urlpatterns = [
    path('story', StoryListCreateView.as_view(), name='story'),
    path('story/<str:pk>', StoryDetailView.as_view(), name='story-details'),
    path('tag', TagListCreateView.as_view()),
]
