from django.contrib import admin
from django.utils.timezone import now
from eventex.subscriptions.models import Subscription

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'email', 'phone', 'created_at', 'subscribed_today','paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at')
    list_filter = ('paid','created_at')

    actions = ['mark_as_paid']

    def subscribed_today(self, obj):
        return obj.created_at == now().date()

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        if count == 1:
            msg = '{} inscrição foi marcada como paga.'
        else:
            msg = '{} incrições foi marcadas como pagas.'

        self.message_user(request, msg.format(count))

    subscribed_today.short_description = 'Inscrito hoje?'
    subscribed_today.boolean = True

    mark_as_paid.short_description = 'Marcar como pago'

admin.site.register(Subscription, SubscriptionModelAdmin)