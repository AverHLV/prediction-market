from django.contrib import admin
from .models import Outcome, Market, Asset, Order


@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    search_fields = 'description',


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    search_fields = 'name',
    list_filter = 'start_date', 'end_date', 'resolved'


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_filter = 'closed',


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
