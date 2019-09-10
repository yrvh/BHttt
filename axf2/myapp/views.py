from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'myapp/home.html')
def market(request):
    return render(request,'myapp/market.html')
def cart(request):
    return render(request,'myapp/cart.html')
def mine(request):
    return render(request,'myapp/mine.html')