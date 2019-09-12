from django.conf.urls import url
from django.contrib import admin
from .import views

app_name = 'myapp'
urlpatterns = [
    url(r'^home/$',views.home,name="home"),
    url(r'^market/$',views.market,name="market"),
    url(r'^cart/$',views.cart,name="cart"),
    url(r'^mine/$',views.mine,name="mine"),
]
