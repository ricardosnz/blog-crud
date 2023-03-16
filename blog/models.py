from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

UserModel = get_user_model()

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    about = models.TextField(null=True, blank=True)
    content = RichTextField(blank=True, null=True)
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.BooleanField(default=True)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, default=4)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.title
