from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from .models import Story, Tag
from .serializers import GeneralStorySerializer, DetailsStorySerializer, GeneralTagSerializer
from .utils import DefaultPagination

class StoryDetailView(generics.RetrieveAPIView):
    serializer_class = DetailsStorySerializer

    def get_queryset(self):
        qs = (
            Story.objects.
            prefetch_related('tags').
            filter(accept=True)
        )
        return qs
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class StoryListCreateView(generics.ListCreateAPIView):
    serializer_class = GeneralStorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'text']
    pagination_class = DefaultPagination

    def get_queryset(self):
        qs = (
            Story.objects.
            prefetch_related('tags').
            filter(accept=True).
            order_by('-created_at')
        )
        return qs

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save(user=None)


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.filter(accept=True)
    serializer_class = GeneralTagSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

