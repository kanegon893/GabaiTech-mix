from django.db import models

class Article(models.Model):
    content = models.CharField(max_length=140)
    user_name = models.CharField(max_length=50, null = True) # nameカラムを追加

    def __str__(self):
        return self.content
