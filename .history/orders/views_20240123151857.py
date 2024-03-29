from django.shortcuts import render
from .models import OrderItem, Order 
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.urls import reverse
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.admin.views.decorators import staff_member_required



def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asyn tasks
            order_created.delay(order.id)
            # set the order in the session 
            request.session['order_id'] = order.id
            # redirect for payment 
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
