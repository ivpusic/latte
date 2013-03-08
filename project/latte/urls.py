from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.views.generic import list_detail
from latte.views import HomeView, LoginView, AddProductView, EditProductView, RestaurantInfoView, DeletePictureView, DeleteProductView
from django.contrib import admin
from django.conf.urls import patterns, url, include

admin.autodiscover()

urlpatterns = patterns("",
                        url(r"^$", LoginView.as_view(), name="login"),
                        url(r"^admin/", include(admin.site.urls)),
                        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
                        url(r"^account/", include("account.urls")),
                        url(r"^home/$", HomeView.as_view(), name="home"),
                        url(r"^home/addProduct", AddProductView.as_view(), name="addProduct"),
                        url(r"^home/editProduct/(?P<pk>\d+)", EditProductView.as_view(), name="editProduct"),
                        url(r"^home/deleteProduct/(?P<pk>\d+)", DeleteProductView.as_view(), name="deleteProduct"),
                        url(r"^home/deletePicture/(?P<pk>\d+)", DeletePictureView.as_view(), name="deletePicture"),
                        url(r"^restaurantInfo/$", RestaurantInfoView.as_view(), name="restaurantInfo"),
                        url(r'^api/', include("RESTService.urls")),               
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
