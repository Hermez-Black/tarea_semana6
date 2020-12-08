from django.shortcuts import render
from Comments.models import Comment
from Comments.serializers import CommentSerializer
from rest_framework import viewsets, status
from Posts.serializers import PostSerializer
from rest_framework.response import Response
from Posts.models import Post
from rest_framework.decorators import action
# Create your views here.
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=['get', 'post', 'delete'])
    def posts(self, request, pk=None):
        comments = self.get_object()
        if req.method == 'GET':
            serializer = PostSerializer(comments.post_comment, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        
        if request.method == 'POST':
            post_id = request.data['post_id']
            for post in post_id:
                post_obtenido = Post.objects.get(id=post)
                comments.post_comment.add(post_obtenido)
            serializer = PostSerializer(comments.post_comment, many=True)
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)

        if request.method == 'DELETE':
            post_id = request.data['post_id']
            for post in post_id:
                post = Post.objects.get(id=post_id)
                comments.post_comment.remove(post)

            return Response(status=status.HTTP_200_OK)

    # @action(detail=True, methods=['get', 'post', 'delete'])
    # def posts(self, request, pk=None):
    #     comments = self.get_object()
    #     if req.method == 'GET':
    #         serializer = PostSerializer(comments.post_comment, many=True)
    #         return Response(status=status.HTTP_200_OK, data=serializer.data)
        
    #     if request.method == 'POST':
    #         post_id = request.data['post_id']
    #         for post in post_id:
    #             post_obtenido = Post.objects.get(id=post)
    #             comments.post_comment.add(post_obtenido)
    #         serializer = PostSerializer(comments.post_comment, many=True)
    #         return Response(status=status.HTTP_201_CREATED, data=serializer.data)

    #     if request.method == 'DELETE':
    #         post_id = request.data['post_id']
    #         for post in post_id:
    #             post = Post.objects.get(id=post_id)
    #             comments.post_comment.remove(post)

    #         return Response(status=status.HTTP_200_OK)


