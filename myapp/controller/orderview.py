from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from myapp.models import  Order,OrderItem
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



def orders(request):
    orders=Order.objects.filter(user=request.user)
    context={'orders':orders}
    return render(request, 'myapp/myorder.html', context)

def vieworder(request, t_no):
    order=Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems=OrderItem.objects.filter(order=order)
    context={'order':order, 'orderitems':orderitems}
    return render(request, 'myapp/orderviews.html', context)

