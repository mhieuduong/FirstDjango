from django.db import models
from django.conf import settings


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, null=True)
    description = models.TextField()
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

    def __str__(self):
        return self.title
