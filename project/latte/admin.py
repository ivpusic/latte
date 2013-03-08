from django.contrib import admin
from latte.models import Product, Restaurant, RestaurantProduct, ProductPicture, Category

admin.site.register(Product)
admin.site.register(Restaurant)
admin.site.register(RestaurantProduct)
admin.site.register(ProductPicture)
admin.site.register(Category)