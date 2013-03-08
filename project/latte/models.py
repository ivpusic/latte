from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from json import JSONEncoder
    
class Restaurant(models.Model):

    user = models.OneToOneField(User)
    
    name = models.CharField(max_length = 100)
    adress = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 50)
    description = models.TextField()

    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    """Create the UserProfile when a new User is saved"""
    if created:
        profile = Restaurant()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

class Product(models.Model):
    
    name = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)
    restaurants = models.ManyToManyField(Restaurant, through="RestaurantProduct", null = True)
    category = models.ForeignKey(Category, related_name="products")
    
    def __unicode__(self):
        return self.name

import os
# Helper method to return the absolute path for upload_to field in ProductPicture model
def getUploadPath(self, filename):
    dir = '%s/%s' % (settings.MEDIA_ROOT, self.product.name)
    if not os.path.exists(dir):
        os.makedirs(dir)
    return '%s/%s/%s' % (settings.MEDIA_ROOT, self.product.name, filename)
    
class ProductPicture(models.Model):
    product_picture = models.FileField(upload_to = getUploadPath, null = True, blank = True)
    relative_path = models.TextField(blank=True)
    product = models.ForeignKey(Product, related_name="pictures")
    
class RestaurantProduct(models.Model):
    price = models.FloatField()
    restaurant = models.ForeignKey(Restaurant)
    product = models.ForeignKey(Product)
    