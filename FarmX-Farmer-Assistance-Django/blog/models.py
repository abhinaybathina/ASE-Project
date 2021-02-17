from django.shortcuts import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from farm.models import Farm
from PIL import Image


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='Farm.jpg', upload_to='blog_pics')
    type = models.CharField(max_length=50, default='Agriculture')
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f'{self.title} by {self.author.username}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=250)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f'Comment on {self.post.title} by {self.user.username}'
