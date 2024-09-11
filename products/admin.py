from django.contrib import admin
from .models import Product, Tariff, Promotion


class TariffInline(admin.TabularInline):
    model = Tariff
    extra = 1


class PromotionInline(admin.TabularInline):
    model = Promotion.tariffs.through
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [TariffInline]


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'product')
    inlines = [PromotionInline]


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount_percentage', 'start_date', 'end_date')
    filter_horizontal = ('tariffs',)


