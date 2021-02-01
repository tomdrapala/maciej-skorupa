from django.db import models
from django.utils import timezone
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    post_text = models.TextField()
    video_address = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                             related_name='projects', null=True, blank=True)
    publish = models.BooleanField(default=False)
    header = models.BooleanField(default=False, null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
