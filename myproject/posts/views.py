from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
import requests


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = []
    serializer_class = PostSerializer

    def get_queryset(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        return response.json()
