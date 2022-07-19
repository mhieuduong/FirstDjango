from django.db import models


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

    def __str__(self):
        return self.title
