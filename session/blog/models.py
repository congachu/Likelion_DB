from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    writer = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, default="없음")
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title