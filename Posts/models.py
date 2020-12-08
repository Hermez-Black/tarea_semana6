from django.db import models
from Tags.models import Tag
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    Autor = models.CharField(max_length=100)
    created = models.DateTimeField(auto_created=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='tags', null=True, blank=True)
    # comments = models.ManyToManyField(Comment, related_name='comments', null=True, blank=True)
    def __str__(self):
        return self.title

