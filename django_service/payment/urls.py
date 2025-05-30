from django.urls import path

from payment.views import CreatePaymentAPIView


urlpatterns = [
    path('api/webhook/bank/', CreatePaymentAPIView.as_view())
]