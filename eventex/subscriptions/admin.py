from django.contrib import admin
from django.utils.timezone import now
from eventex.subscriptions.models import Subscription

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'email', 'phone', 'created_at', 'subscribed_today','paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at')
    list_filter = ('created_at', 'paid')

    def subscribed_today(self, obj):
        return obj.created_at == now().date()

    subscribed_today.short_description = 'Inscrito hoje?'
    subscribed_today.boolean = True

admin.site.register(Subscription, SubscriptionModelAdmin)