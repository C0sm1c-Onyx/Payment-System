from rest_framework import serializers

from organization.models import Balance, Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class BalanceSerializer(serializers.ModelSerializer):
    inn = OrganizationSerializer().fields.get('inn')

    class Meta:
        model = Balance
        fields = ('inn', 'balance')