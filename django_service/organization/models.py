from django.db import models


class Organization(models.Model):
    inn = models.CharField(max_length=12)
    ogrn = models.CharField(max_length=13, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    organization_name = models.CharField(max_length=100)
    organization_desc = models.TextField(max_length=5000, blank=True, null=True)
    director_fio = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=319, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.inn}"


class Balance(models.Model):
    inn = models.OneToOneField(Organization, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.balance}"
