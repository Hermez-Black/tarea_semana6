from django.shortcuts import render
from Posts.models import Post
from Posts.serializers import PostSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from Comments.models import Comment
from Tags.serializers import TagSerializer
from Tags.models import Tag
# Create your views here.
class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # @action(detail=True, methods=['get'])
    # def get_post_comment(self, request, pk=None):
    #     post = self.get_object()
    #     serializer = CommentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         return Response({'post': post.title,
    #         'comment': serializer.content})
    #     else: 
    #         return Response(serializer.errors, 
    #                     status=status.HTTP_400_BAD_REQUEST)

    
    @action(detail=True, methods=['get', 'post', 'delete'])
    def tags(self, request, pk=None):
        post = self.get_object()
        if request.method == 'GET':
            serializer = TagSerializer(post.tags, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        
        if request.method == 'POST':
            tag_id = request.data['tag_id']
            for tag in tag_id:
                tag_obtenido = Tag.objects.get(id=tag)
                post.tags.add(tag_obtenido)
            serializer = TagSerializer(post.tags, many=True)
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)

        if request.method == 'DELETE':
            tag_id = request.data['tag_id']
            for tag in tag_id:
                tag_obtenido = Tag.objects.get(id=tag)
                post.tags.remove(tag_obtenido)

            return Response(status=status.HTTP_200_OK)
