from django.urls import path
from . import views
from . import wehbooks 

app_name = 'payment'


urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('completed/', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('wehbook/', wehbooks.stripe_wehbook, name='stripe-wehbook'),
]
