from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http.response import JsonResponse
from django.db.models import Min, Max


# Create your views here.

def home(request):
    trending_products=Product.objects.filter(trending=1)
    context={'trending_products':trending_products}
    return render(request, "myapp/index.html", context)


def collection(request): 
    category=Category.objects.filter(status=0)
    return render(request, "myapp/collection.html", {'category':category})

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        product=Product.objects.filter(category__slug=slug)
        category_name=Category.objects.filter(slug=slug).first()
        return render(request, "myapp/product/product.html", {'product':product, 'category':category_name})
    
    else:
        messages.warning(request, "no such category found")
        return redirect('collections')
    

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products=Product.objects.filter(slug=prod_slug, status=0).first
            context={'products':products}
        else:
             messages.error(request, "no such product found")
             return redirect('collection')
    else:
        messages.error(request, "no such product found")
        return redirect('collection')
    
    return render(request, "myapp/view.html" ,{'products':products})


# def searchproductajax(request):
#     products=Product.objects.filter(status=0).values_list('name',flat=True)
#     productList=list(products)
    
#     return JsonResponse(productList, safe=False)
    

    
# def searchproduct(request):
#     if request.method == 'POST':
#         searchedterm = request.POST.get('productsearch', '').strip()  # Strip to remove extra spaces
#         if not searchedterm:  # Better check for an empty search term
#             return redirect(request.META.get('HTTP_REFERER', '/'))  # Fallback in case HTTP_REFERER is missing
        
#         # Search for the product using case-insensitive partial matching
#         product = Product.objects.filter(name__icontains=searchedterm).first()
        
#         if product:
#             # Redirect to the product page
#             return redirect('collection/' + product.category.slug + '/' + product.slug)
#         else:
#             # No product found, display a message and redirect
#             messages.info(request, "No product matched your search")
#             return redirect(request.META.get('HTTP_REFERER', '/'))
    
    # Default redirect if the request method is not POST
    # return redirect(request.META.get('HTTP_REFERER', '/'))
    
def searchproductajax(request):
    # Fetching the product names for the autocomplete, filtering only active products (status=0)
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    productList = list(products)
    
    return JsonResponse(productList, safe=False)


def searchproduct(request):
    if request.method == 'POST':
        searchedterm = request.POST.get('productsearch', '').strip()  # Strip spaces
        if not searchedterm:  # Check for empty search terms
            return redirect(request.META.get('HTTP_REFERER', '/'))  # Redirect to the referring page
        
        # Searching products case-insensitively
        product = Product.objects.filter(name__icontains=searchedterm).first()
        
        if product:
            # Redirect to the product page with correct slug paths
                return redirect(f'/collection/{product.category.slug}/{product.slug}')
        else:
            # No product found, display a message and redirect
            messages.info(request, "No product matched your search")
            return redirect(request.META.get('HTTP_REFERER', '/'))
        
        

def product_listfilter(request):
    products = Product.objects.filter(status=0)  # Fetch all active products

    # Get minimum and maximum price from GET parameters
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)

    # Apply price filters if both are provided
    if min_price and max_price:
        try:
            min_price = float(min_price)
            max_price = float(max_price)
            products = products.filter(selling_price__gte=min_price, selling_price__lte=max_price)
        except ValueError:
            pass  # Handle invalid input (non-numeric values)

    return render(request, 'filterprice.html', {'products': products})