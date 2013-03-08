from latte.models import Restaurant, Product, RestaurantProduct, ProductPicture, Category
from rest_framework import serializers

class RestaurantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Restaurant

class ProductPictureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductPicture
        fields = ("relative_path", "id")

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

class ProductSerializerHelper(serializers.Field):
    
    def to_native(self, value):
        if isinstance(value, Product):
            serializer = ProductSerializer(value)
            return serializer.data
        else:
            return super(ProductSerializerHelper, self).to_native(value)
    
class ProductPictureSerializerHelper(serializers.Field):
    
    def to_native(self, value):
        if isinstance(value, ProductPicture):
            serializer = ProductPictureSerializer(value)
            return serializer.data
        else:
            return super(ProductPictureSerializerHelper, self).to_native(value)

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        depth = 1

class CategorySerializerHelper(serializers.Field):
    
    def to_native(self, value):
        if isinstance(value, Category):
            serializer = CategorySerializer(value)
            return serializer.data
        else:
            return super(ProductPictureSerializerHelper, self).to_native(value)

class RestaurantProductSerializer(serializers.ModelSerializer):
    
    pictures = ProductPictureSerializerHelper(source="product.pictures.all")

    class Meta:
        model = RestaurantProduct
        exclude = ('restaurant', 'id',)
        depth = 1
