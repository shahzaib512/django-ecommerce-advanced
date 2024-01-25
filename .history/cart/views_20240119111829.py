# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.http import require_POST
# from shop.models import Product
# from .cart import Cart
# from .forms import CartAddProductForm


# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product, quantity=cd['quantity'])
#         return redirect('cart:cart_detail')

# @require_POST
# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect('cart:cart_detail')

# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, 'cart/detail.html', {'cart': cart})
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'])
        return redirect('cart:cart_detail')
    else:
        # If the form is not valid, you should handle this case.
        # For example, you can redirect back to the product detail page with an error message.
        return redirect('shop:product_detail', product_id=product.id)
