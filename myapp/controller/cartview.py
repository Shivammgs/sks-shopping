from django.shortcuts import render,redirect
from django.contrib import messages
from django.http.response import JsonResponse
from myapp.models import  Product,Cart
from django.contrib.auth.decorators import login_required



def addtocart(request):
    if request.method =='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check= Product.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status':'Product already in cart'})
                else:   
                    prod_qty=int(request.POST.get('product_qty'))
                    
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status':'Product added successfully'})
                    else:
                      return JsonResponse({'status':'Only '+str(product_check.quantity)+'quantity available'})
            else:
                return JsonResponse({'status':'No Such product found'})
        else:
            return JsonResponse({'status':'Login to continue'})
    
    return redirect('/')

@login_required(login_url='login')

def viewcart(request):
    cart=Cart.objects.filter(user=request.user)
    return render(request, 'myapp/cart.html', {'cart':cart})


def updatecart(request):
    if request.method =='POST':
        prod_id=int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty=int(request.POST.get('product_qty'))
            cart=Cart.objects.filter(product_id=prod_id, user=request.user).first()
            cart.product_qty=prod_qty
            cart.save()
            return JsonResponse({'status':'Updated Successfully'})
    return redirect('/')


# def deletecartitem(request):
#     if request.method =='POST':
#         prod_id=int(request.POST.get('product_id'))
#         if(Cart.objects.filter(user=request.user, product_id=prod_id)):
#             cartitem=Cart.objects.get(product_id=prod_id, user=request.user)
#             cartitem.delete()
#             return JsonResponse({'status':'Item Deleted Successfully'})
#     return redirect('/')

# @login_required(login_url='login')
# def cart_count(request):
#     count = Cart.objects.filter(user=request.user).count()  # Count items in the user's cart
#     return JsonResponse({'count': count})

# @login_required(login_url='login')
def deletecartitem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        cart_item = Cart.objects.filter(user=request.user, product_id=prod_id).first()
        if cart_item:
            cart_item.delete()
            return JsonResponse({'status': 'Item Deleted Successfully'})
    return redirect('/')

@login_required(login_url='login')
def cart_count(request):
    if request.user.is_authenticated:
        count = Cart.objects.filter(user=request.user).count()  # Count items in the user's cart
    else:
        count = 0  # If the user is not authenticated, set count to 0
    return JsonResponse({'count': count})
            


