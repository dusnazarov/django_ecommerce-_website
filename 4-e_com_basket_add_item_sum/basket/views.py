from django.shortcuts import render
from .basket import Basket
from django.shortcuts import get_object_or_404
from store.models import Product
from django.http import JsonResponse


def basket_summary(request):   
    return render(request, 'store/basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty) 
        basketqty = basket.__len__()       
        response = JsonResponse({'test':'data', 'qty': product_qty, 'basket_qty':basketqty})
        return response
    
