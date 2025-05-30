from django.db import models

from organization.models import Organization


class Payment(models.Model):
    operation_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payer_inn = models.CharField(max_length=12)
    document_number = models.CharField(max_length=100)
    document_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class TransactionLogInfo(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    was_balance = models.DecimalField(max_digits=15, decimal_places=2)
    became_balance = models.DecimalField(max_digits=15, decimal_places=2)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

