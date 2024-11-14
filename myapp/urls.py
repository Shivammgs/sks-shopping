from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views
from myapp.controller import authview, cartview, wishlistview, checkoutview, orderview
from myapp.controller import authview as user_views

urlpatterns = [
    path('', views.home, name='home'),
    path('collection/', views.collection, name='collection'),
    path('collection/<str:slug>/', views.collectionsview, name='collectionviews'),
    path('collection/<str:cate_slug>/<str:prod_slug>/', views.productview, name='productviews'),
    
    path('product-list/', views.searchproductajax, name='product_list'),  
    path('searchproducts/', views.searchproduct, name='searchproducts'),
    # path('price-filter/', views.searchproductajax, name='product_list'), 
    path('productsfilter/', views.product_listfilter, name='productfilter'), 

    
    path('register/', user_views.register, name='register'),
    path('login/', user_views.loginpage, name='login'),
    path('logout/', user_views.logoutpage, name='logout'),
    path('changepassword/', user_views.changepassword, name='changepassword'),

    path('add-to-cart/', cartview.addtocart, name='addtocart'),
    path('cart/', cartview.viewcart, name='cart'),
    path('update-cart/', cartview.updatecart, name='updatecart'),
    path('delete-cart-item/', cartview.deletecartitem, name='deletecartitem'),
    path('cart-count/', cartview.cart_count, name='cart_count'),

    
    path('wishlist/', wishlistview.wishlists, name='wishlist'),
    path('add-to-wishlist/', wishlistview.wishlsts, name='addtowishlist'),
    path('delete-wishlist-item/', wishlistview.deletewishlists, name='deletewishlistitem'),
    
    path('checkout/', checkoutview.checklist, name='checkout'),
    path('place-order/', checkoutview.placeorder, name='placeorder'),
    path('proceed-to-pay/', checkoutview.razorpaycheck, name='proceed_to_pay'),
    
    path('my-order/', orderview.orders, name='myorders'),
    path('view-order/<str:t_no>/', orderview.vieworder, name='orderview'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    # path('productfilter', views.product_list, name='product_list'),
]
