from django.db import models


class Post(models.Model):
    userId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
