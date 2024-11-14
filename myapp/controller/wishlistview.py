from django.shortcuts import render,redirect
from django.contrib import messages
from django.http.response import JsonResponse
from myapp.models import  Product,Cart,Wishlist
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')

def wishlists(request):
    wishitems=Wishlist.objects.filter(user=request.user)
    context={'wishitems':wishitems}
    return render(request, 'myapp/wishlist.html', context)


def wishlsts(request):
    if request.method == 'POST':
        if request.user.is_authenticated: 
           prod_id=int(request.POST.get('product_id'))
           product_check=Product.objects.get(id=prod_id)
           if(product_check):
               if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                   return JsonResponse({'status':"Product already in wishlist"})
               else:
                   Wishlist.objects.create(user=request.user, product_id=prod_id)
                   return JsonResponse({'status':"Product added to wishlist"})
           else:
               return JsonResponse({'status':"No Such Product Found"})
        else:
            return JsonResponse({'status':"Login to Continue"})
    return redirect('/')


def deletewishlists(request):
    if request.method =='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            if(Wishlist.objects.filter(user=request.user, product_id=prod_id)).exists():
                wishlistitem=Wishlist.objects.get(product_id=prod_id, user=request.user)
                wishlistitem.delete()
                return JsonResponse({'status':'Product Removed from Wishlist'})
            else:
                return JsonResponse({'status':'Product not found in wishlist'})
        else:
            return JsonResponse({'status':'Login to continue'})

    return redirect('/')