from django.contrib import admin
from chain.models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['title',]
    list_filter = ['contact__city']
    actions = ['log_action']

    def log_action(self, request, queryset):
        for obj in queryset:
            obj.backlog = 0.00
            obj.save()

    log_action.short_description = 'Удалить задолженность у поставщика'
