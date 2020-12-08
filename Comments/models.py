from django.db import models
from Posts.models import Post
# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_created=True, null=True)

    post_comment = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
