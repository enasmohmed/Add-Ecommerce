from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
# Create your models here.
from ecommerce.utils import unique_slug_generator



class Category(models.Model):
    name = models.CharField(max_length=600,blank=False,default=None)
    name_ar = models.CharField(max_length=600,blank=False,default=None)
    name_fi = models.CharField(max_length=600,blank=False,default=None)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,blank=True,null=True, related_name='childern')
    full_name_string = models.CharField(max_length=255,blank=True)

    def full_name_string_fun(self):
        name_list = [self.name]
        parent = self.parent
        while parent is not None:
            name_list.append(parent.name)
            parent = parent.parent
        return name_list

    def __str__(self):
        return ' --> '.join(reversed(self.full_name_string_fun()))


    def save(self,*args,**kwargs):
        self.full_name_string=' '.join(reversed(self.full_name_string_fun()))
        super(Category,self).save(*args,**kwargs)

    class Meta:
        unique_together = ('name', 'parent',)


class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    name_ar = models.CharField(max_length=200, db_index=True)
    name_fi = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(blank=True, unique=True)
    Image = models.ImageField(blank=True, upload_to='media/images/', null=True)
    description = models.TextField(blank=True)
    description_ar = models.TextField(blank=True)
    description_fi = models.TextField(blank=True)
    price = models.FloatField()
    old_price = models.FloatField()
    currency = models.CharField(max_length=5)
    currency_ar = models.CharField(max_length=128)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    popular = models.BooleanField(default=True)
    related = models.BooleanField(default=True)
    upsell = models.BooleanField(default=True)
    interested = models.BooleanField(default=True)


    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Shop:product_detail', args=[self.id, self.slug])



def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender= Product)




class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='productimages',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return self.product.name