from django.urls import path
from .views import OrderListView, OrderDetailView, AddToCart, ViewCart, RemoveFromCart, OrderCreateView, \
    PaymentView \
    # , Checkout

urlpatterns = [

    path('orders/', OrderListView.as_view(), name='order-list-create'),
    path('orders-detail/<int:pk>/', OrderDetailView.as_view(), name='order-retrieve-update-destroy'),
    path('orders-create/', OrderCreateView.as_view(), name='order-create'),
    path('add-to-cart/', AddToCart.as_view(), name='add_to_cart'),
    path('view-cart/', ViewCart.as_view(), name='view_cart'),
    path('remove-from-cart/<int:pk>/', RemoveFromCart.as_view(), name='remove_from_cart'),
    # path('checkout/', Checkout.as_view(), name='checkout'),
    path('payment/', PaymentView.as_view(), name='payment'),

]
