from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    comment = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank=True)
    available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('Shop:home')
