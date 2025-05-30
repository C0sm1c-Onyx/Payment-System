from django.contrib import admin

from payment.models import Payment, TransactionLogInfo


class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'operation_id', 'amount', 'payer_inn',
        'document_number', 'document_date'
    )
    list_display_links = (
        'operation_id', 'amount', 'payer_inn',
        'document_number', 'document_date'
    )
    search_fields = ('operation_id', 'payer_inn', 'amount')


admin.site.register(Payment, PaymentAdmin)