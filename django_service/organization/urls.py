from django.urls import path

from organization.views import BalanceAPIView


urlpatterns = [
    path('api/organizations/<int:inn>/balance/', BalanceAPIView.as_view())
]