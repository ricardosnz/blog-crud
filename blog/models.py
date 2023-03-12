from django.db import models

from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    about = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
