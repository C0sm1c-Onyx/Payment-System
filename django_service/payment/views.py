from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from payment.serializers import PaymentSerializer
from payment.models import Payment


class CreatePaymentAPIView(CreateAPIView):
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        if not self.is_exists_operation(data):
            Payment.objects.create(**data)

        return Response(data)

    def is_exists_operation(self, data):
        if Payment.objects.filter(operation_id=data['operation_id']):
            return True

        return False
