from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey("web.Category",on_delete=models.CASCADE)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = "web_category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name 
