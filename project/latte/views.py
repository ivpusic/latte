import account.views
import account.forms
from account.forms import SignupForm, LoginUsernameForm
from django.shortcuts import redirect
from django.views.generic import ListView, View, TemplateView, DetailView
from latte.models import Product, ProductPicture, Restaurant, RestaurantProduct, Category
from .forms import CreateProductForm, RestaurantInfoForm
from django.http import HttpResponse
from latte import settings

"""
Method for getting restaurant for logged user
"""
def getRestaurant(request):
    loggedUser = request.user
    return Restaurant.objects.get(user = loggedUser)

class LoginView(account.views.LoginView):
    
    template_name = "loginpage.html"
    form_class = account.forms.LoginUsernameForm
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            
            context = { 
                'user': self.request.user,
             }
            return redirect("home")
        
        else:
            context = {
                    'login_form': LoginUsernameForm,
                    'signup_form': SignupForm, 
            }
            return self.render_to_response(context)
            
class HomeView(ListView):

    userId = ""
    template_name = "homepage.html"
    context_object_name = "restProducts"

    def get_queryset(self):
        try:
            r = getRestaurant(self.request)
            return RestaurantProduct.objects.filter(restaurant = r)
        except:
            restaurant = Restaurant()
            restaurant.user = self.request.user
            restaurant.save()

class AddProductView(TemplateView):
    
    template_name = "addProduct.html"

    def post(self, request, *args, **kwargs):        
        frm = CreateProductForm(request.POST)
        
        if frm.is_valid():
            product_name = self.request.POST["name"]
            product_description = self.request.POST["description"]
            cat = Category.objects.get(pk=int(self.request.POST["category"]))
            p = Product.objects.create(name = product_name, description = product_description, category = cat)
            p.save()
            for uploaded_file in self.request.FILES.getlist('file_upload'):
                rp = '%s/%s/%s' % (settings.MEDIA_URL_UPLOAD, product_name, uploaded_file.name)
                productPicture = ProductPicture(product_picture = uploaded_file, relative_path=rp, product = p)
                productPicture.save(force_insert=True)

            r = getRestaurant(self.request)
            rp = RestaurantProduct.objects.create(price = self.request.POST["price"],
            restaurant=r, product=p)
            rp.save()
            return redirect("home")
            
        else:
            ctx = super(AddProductView, self).get_context_data(**kwargs)
            ctx['createProduct_form'] = CreateProductForm(request.POST)
            return self.render_to_response(ctx)

    def get_context_data(self, **kwargs):
        ctx = super(AddProductView, self).get_context_data(**kwargs)
        ctx['createProduct_form'] = CreateProductForm()
        return ctx

class EditProductView(DetailView):

    template_name = "editProduct.html"
    model = Product

    def get_context_data(self, **kwargs):
        ctx = super(EditProductView, self).get_context_data(**kwargs)
        
        p = Product.objects.get(pk=self.kwargs["pk"])
        r = getRestaurant(self.request)
        rp = RestaurantProduct.objects.get(product = p, restaurant = r)
        
        data = p.__dict__
        data["category"] = p.category.id
        print data
        data["price"] = rp.price
        ctx["productId"] = p.id
        frm = CreateProductForm(data)
        ctx["form"] = frm
        return ctx

    def post(self, request, *args, **kwargs):
        frm = CreateProductForm(request.POST)

        if frm.is_valid():
            p = Product.objects.get(pk = request.POST["id"])
            if "name" in request.POST:
                p.name = self.request.POST["name"]
            if "category" in request.POST:
                p.category = Category.objects.get(pk=int(self.request.POST["category"]))
            if "description" in request.POST:
                p.description = self.request.POST["description"]
            p.save()

            for uploaded_file in self.request.FILES.getlist('file_upload'):
                rp = '%s/%s/%s' % (settings.MEDIA_URL_UPLOAD, p.name, uploaded_file.name)
                productPicture = ProductPicture(product_picture = uploaded_file, relative_path=rp, product = p)
                productPicture.save(force_insert=True)
                
            r = getRestaurant(self.request)

            rp = RestaurantProduct.objects.get(restaurant=r, product=p)
            if "price" in request.POST:
                rp.price = self.request.POST["price"]
            rp.save()
            
            return redirect("home")
            
        else:
            ctx = super(EditProductView, self).get_context_data(**kwargs)
            ctx['form'] = CreateProductForm(request.POST)
            return self.render_to_response(ctx)


class RestaurantInfoView(TemplateView):
    
    template_name = "restaurantInfo.html"
    
    def get_context_data(self, **kwargs):
        ctx = super(RestaurantInfoView, self).get_context_data(**kwargs)
        
        r = getRestaurant(self.request)
        ctx["restaurantId"] = r.id
        ctx["form"] = RestaurantInfoForm(instance=r)
        return ctx

    def post(self, request, *args, **kwargs):
        frm = RestaurantInfoForm(request.POST)

        if frm.is_valid():
            r = getRestaurant(self.request)

            if "name" in request.POST:
                r.name = self.request.POST["name"]

            if "description" in request.POST:
                r.description = self.request.POST["description"]

            if "adress" in request.POST:
                r.adress = self.request.POST["adress"]

            if "phone_number" in request.POST:
                r.phone_number = self.request.POST["phone_number"]

            r.save()            
            return redirect("home")
            
        else:
            ctx = super(RestaurantInfoView, self).get_context_data(**kwargs)
            ctx['form'] = RestaurantInfoForm(request.POST)
            return self.render_to_response(ctx)

"""
View for deleting pictures -> ajax POST request
"""
class DeletePictureView(View):
    
    def post(self, request, pk, *args, **kwargs):
        if(request.user.is_authenticated()):
            ProductPicture.objects.get(id=pk).delete()
            return HttpResponse("Success")
        else:
            return HttpResponse("You are not authenticated")

"""
View for deleting some product for some restaurant 
"""
class DeleteProductView(View):

    def post(self, request, pk, *args, **kwargs):
        if(request.user.is_authenticated()):
            r = getRestaurant(request)
            p = Product.objects.get(id=pk)
            RestaurantProduct.objects.get(restaurant = r, product = p).delete()
            return HttpResponse("Success")
        else:
            return HttpResponse("You are not authenticated")
            
        
