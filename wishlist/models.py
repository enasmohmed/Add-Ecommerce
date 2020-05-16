from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from Shop.models import Product
from ecommerce import settings

# User = settings.AUTH_USER_MODEL

class WishListManager(models.Manager):
    def new_or_get(self, request):
        if request.user.is_authenticated:
            user = request.user
            qs = self.get_queryset().filter(user=user)
            if qs.count() == 1:
                new_list = False
                list = qs.first()
                if request.user.is_authenticated and list.user is None:
                    list.user = request.user
                    list.save()
            else:
                list = WishList.objects.new(user=request.user)
                new_list = True
            return list, new_list
        else:
            pass

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

class WishList(models.Model):
    user = models.ForeignKey(User ,related_name='wishlistusers', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

    objects = WishListManager()

    def __str__(self):
        return self.user.email

    class Meta:
        ordering = ['-id']