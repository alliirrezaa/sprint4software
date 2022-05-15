from django.urls import path
from . import views

app_name='cart'
urlpatterns = [
    path('',views.CartDetail.as_view(),name='cart_detail'),
    path('add/<int:id>/',views.add_cart,name='add_cart'),
    path('remove/<int:id>/',views.remove_cart,name='remove_cart'),
]
