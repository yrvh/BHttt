from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'myapp/home.html',{"title":"主页"})
def market(request):
    return render(request,'myapp/market.html',{"title":"闪送超市"})
def cart(request):
    return render(request,'myapp/cart.html',{"title":"购物车"})
def mine(request):
    return render(request,'myapp/mine.html',{"title":"我的"})