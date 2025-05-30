from django.contrib import admin

from organization.models import Balance, Organization


class BalanceAdmin(admin.ModelAdmin):
    list_display = ('inn', 'balance')
    list_display_links = ('inn', 'balance')
    search_fields = ('balance',)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('inn', 'organization_name', 'director_fio', 'created_at')
    list_display_links = ('inn', 'organization_name', 'director_fio', 'created_at')
    search_fields = ('inn', 'organization_name')


admin.site.register(Balance, BalanceAdmin)
admin.site.register(Organization, OrganizationAdmin)
