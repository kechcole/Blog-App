from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Automatically populate date
    date_posted = models.DateTimeField(default=timezone.now)
    # Foreign key
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Dunder method that make query result descriptive.
    def __str__(self):
        return self.title
    
    # Plural naming 
    class Meta:
        verbose_name_plural = "Post"
