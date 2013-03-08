from rest_framework import generics
from RESTService.serializers import RestaurantSerializer, CategorySerializer, ProductSerializer, RestaurantProductSerializer
from latte.models import Restaurant, Product, ProductPicture, RestaurantProduct, Category
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, JSONPRenderer, BrowsableAPIRenderer
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView


class RestaurantList(generics.ListAPIView):
    """
    API endpoint that represents a list of restaurants
    """
    renderer_classes = (JSONPRenderer, JSONRenderer, BrowsableAPIRenderer)
    model = Restaurant
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveAPIView):
    """
    API endpoint that represents a single restauran.
    """
    renderer_classes = (JSONPRenderer, JSONRenderer, BrowsableAPIRenderer)
    model = Restaurant
    serializer_class = RestaurantSerializer

class ProductList(APIView):
    """
    API endpoint that retrieve list of products for some restaurant
    """
    renderer_classes = (JSONPRenderer, JSONRenderer, BrowsableAPIRenderer)
    def get(self, request, pk, *args, **kwargs):
        rest = Restaurant.objects.get(id=pk)
        queryset = RestaurantProduct.objects.filter(restaurant=rest)
        serializer = RestaurantProductSerializer(queryset)
        return Response(serializer.data)

class CategoryList(APIView):
    """
    API endpoint that retrieve list of categories for restaurant
    """
    renderer_classes = (JSONPRenderer, JSONRenderer, BrowsableAPIRenderer)
    def get(self, request, pk, *args, **kwargs):
        rest = Restaurant.objects.get(id=pk)
        products = Product.objects.filter(restaurants=rest)
        queryset = Category.objects.filter(products__in=products).distinct()
        serializer = CategorySerializer(queryset)
        return Response(serializer.data)

class CategoryProducts(APIView):
    """
    API endpoint that retrieve list of product for some category
    """
    renderer_classes = (JSONPRenderer, JSONRenderer, BrowsableAPIRenderer)
    def get(self, request, pk, cid, *args, **kwargs):
        cat = Category.objects.get(id=cid)
        rest = Restaurant.objects.get(id=pk)
        queryset = Product.objects.filter(category=cat, restaurants=rest)
        serializer = ProductSerializer(queryset)
        return Response(serializer.data)


class ProductDetail(APIView):
    """
    API endpoint that retrieve details for some product
    """
    renderer_classes = (JSONPRenderer, JSONRenderer, BrowsableAPIRenderer)
    def get(self, request, rid, pid, *args, **kwargs):
        try:
            prod = Product.objects.get(pk=pid)
            rest = Restaurant.objects.get(pk=rid)
            queryset = RestaurantProduct.objects.filter(restaurant=rest, product=prod)
            serializer = RestaurantProductSerializer(queryset)
            return Response(serializer.data)
        except:
            return Response("No results")
