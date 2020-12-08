from django.shortcuts import render
from Tags.models import Tag
from Tags.serializers import TagSerializer
from rest_framework import viewsets

# Create your views here.
class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

