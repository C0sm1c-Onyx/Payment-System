from rest_framework.views import APIView
from rest_framework.response import Response

from organization.models import Balance
from organization.serializers import BalanceSerializer


class BalanceAPIView(APIView):
    serializer_class = BalanceSerializer

    def get(self, request, inn, *args, **kwargs):
        data = self.serializer_class(self.get_queryset(inn__inn=inn), many=True).data
        return Response(
            data[0] if data else {}
        )

    def get_queryset(self, *args, **kwargs):
        return Balance.objects.filter(**kwargs)




