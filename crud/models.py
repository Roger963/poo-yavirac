from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=200)
    slug = models.BooleanField(default=True)
    content = models.CharField(max_length=200)
    def __str__(self):
        return self.title
