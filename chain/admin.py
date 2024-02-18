from django.contrib import admin

from chain.models import Partner, Contact


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_contact']
    # list_filter = ['foreign_key__contact']


    @admin.display(description='город')

    def get_contact(self, obj):
        return [contact.city for contact in obj.contact_set.all()]

