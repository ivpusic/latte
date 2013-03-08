'''
from latte.models import Restaurant
from djangorestframework.resources import ModelResource


class RestaurantResource(ModelResource):
    model = Restaurant
    fields = ('adress', 'description', 'name', 'phone_number', 'id')
'''