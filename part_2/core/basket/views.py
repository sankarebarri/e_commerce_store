from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .basket import Basket
from store.models import Product

def basket_summary(request):

    return render(request, 'store/basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productId'))
        product_qty = int(request.POST.get('productQty'))
        # print(product_qty)
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, product_qty=product_qty)
        response = JsonResponse({
            'quantity': product_qty
        })
        return response