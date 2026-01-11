from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def reading_time(self):
        words = len(self.content.split())
        return max(1, words // 200)
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comment by {self.name}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        unique_together = ("user", "post")

    def __str__(self):
        return f"{self.user} likes {self.post}"