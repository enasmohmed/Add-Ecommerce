from random import choices

from django.db import models
from Shop.models import Product
from decimal import Decimal
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.


class order(models.Model):
    CITY_CHOICES = [
        ('الرياض', 'الرياض'),
        ('الجبيل', 'الجبيل'),
        ('الطائف', 'الطائف'),
        ('حايل', 'حايل'),
        ('جده', 'جده'),
        ('الدمام', 'الدمام'),
        ('المدينة المنورة', 'المدينة المنورة'),
        ('حفر الباطن', 'حفر الباطن'),
        ('تبوك', 'تبوك'),
        ('جيزان', 'جيزان'),
        ('الخرج', 'الخرج'),
        ('نجران', 'نجران'),
        ('ابها', 'ابها'),
        ('مكه', 'مكه'),
        ('الاحساء', 'الاحساء'),
        ('القصيم', 'القصيم'),
        ('بيشه', 'بيشه')
    ]

    COUNTRY_CHOICES = [
        ('السعودية', 'السعودية')
    ]

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(choices=CITY_CHOICES, max_length=120)
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=120,default='السعودية')
    created = models.DateTimeField(auto_now_add=True, null=True,)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
