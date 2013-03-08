from django.conf.urls import patterns, include, url
from RESTService.views import RestaurantList, RestaurantDetail, ProductList, ProductDetail, CategoryList, CategoryProducts
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import patterns, url, include

urlpatterns = patterns("",
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^restaurants/$', RestaurantList.as_view(), name='restaurant-list'),
                       url(r'^restaurant/(?P<pk>\d+)/$', RestaurantDetail.as_view(), name='restaurant-detail'),
                       url(r'^restaurant/(?P<pk>\d+)/products/$', ProductList.as_view(), name='restaurant-detail'),
                       url(r'^restaurant/(?P<pk>\d+)/categories/$', CategoryList.as_view(), name='category-detail'),
                       url(r'^restaurant/(?P<pk>\d+)/category/(?P<cid>\d+)/products$', CategoryProducts.as_view(), name='category-detail'),
                       url(r'^restaurant/(?P<rid>\d+)/product/(?P<pid>\d+)$', ProductDetail.as_view(), name='product-detail'),
)
