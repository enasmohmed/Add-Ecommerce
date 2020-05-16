from django.contrib import admin

from Shop.models import Product, Category, ProductImage

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Product




admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)