from django.db import models #type: ignore

# Create your models here.
class UrlData(models.Model):
    original_url = models.URLField(max_length=2000)
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_url
