from django.db import models


class Post(models.Model):
    """
    id: key
    title: varchar 255
    description: text
    created_at: datetime
    updated_at: datetime
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

    def __str__(self):
        return self.title
