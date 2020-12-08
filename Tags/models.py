from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=80)
    created = models.DateTimeField(auto_created=True, null=True)

    def __str__(self):
        return self.name
