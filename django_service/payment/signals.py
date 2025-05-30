from django.db.models.signals import post_save
from django.dispatch import receiver

from payment.models import Payment, TransactionLogInfo
from organization.models import Balance, Organization


@receiver(post_save, sender=Payment)
def execute_transaction(sender, instance, created, *args, **kwargs):
    if created:
        org_balance = Balance.objects.get(inn__inn=instance.payer_inn)

        was_bal = org_balance.balance
        became_bal = was_bal + instance.amount

        org_balance.balance = became_bal
        org_balance.save()

        TransactionLogInfo.objects.create(
            payment=instance,
            was_balance=was_bal,
            became_balance=became_bal,
            organization=Organization.objects.get(inn=instance.payer_inn)
        )


