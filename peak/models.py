from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager


class Peak(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
