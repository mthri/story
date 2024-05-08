from django.urls import path

from .views import StoryListCreateView, StoryDetailView, TagListCreateView


urlpatterns = [
    path('story', StoryListCreateView.as_view()),
    path('story/<str:pk>', StoryDetailView.as_view()),
    path('tag', TagListCreateView.as_view()),
]
