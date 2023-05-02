from django.db import models
from users.models import User


class ItemModel(models.Model):
    photo = models.ImageField(upload_to='users_images', null=True, blank=True)
    title = models.CharField(max_length=27)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True)
    place = models.CharField(max_length=25, null=True, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
