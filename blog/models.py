from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    pid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    content = models.TextField()
    thumbnail = ResizedImageField(size=[600, 500], quality=100, upload_to='post_pics', blank=True)
    thumbnail_url = models.URLField(blank=True)
    category = models.CharField(max_length=20)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Postdetails", kwargs={"pk": self.pk})




