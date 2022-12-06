from django.shortcuts import render
from django.views import View
from app.models import Product,OrderPlace,Customer,Cart

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        topwear=Product.objects.filter(categary='TW')
        bottomwear=Product.objects.filter(categary='BW')
        mobile=Product.objects.filter(categary='M')
        laptop=Product.objects.filter(categary='L')

         
        return render(request,'app/home.html',{'topwear':topwear,'bottomwear':bottomwear,'mobile':mobile,'laptop':laptop})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class ProductDetailView(View):
    def get(self,request,id):
        product=Product.objects.get(id=id)

        return render(request, 'app/productdetail.html',{'product':product})


def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
    if data==None:
        mobile=Product.objects.filter(categary="M")
    elif data=='samsang' or data=='redmi':
        mobile=Product.objects.filter(categary="M").filter(brand=data)
    
    elif data=='below':
        mobile=Product.objects.filter(categary="M").filter(selling_price__lt='10000')

    elif data =='above':
        mobile=Product.objects.filter(categary="M").filter(selling_price__gte='10000')
    return render(request, 'app/mobile.html', {'mobile':mobile})

def laptop(request,data=None):
    if data==None:
        laptop=Product.objects.filter(categary="L")
    elif data=='hp' or data=='dell':
        laptop=Product.objects.filter(categary="L").filter(brand=data)
    
    elif data=='below':
        laptop=Product.objects.filter(categary="L").filter(selling_price__lt='20000')

    elif data =='above':
        laptop=Product.objects.filter(categary="L").filter(selling_price__gte='20000')
    return render(request, 'app/laptop.html', {'laptop':laptop})


def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
