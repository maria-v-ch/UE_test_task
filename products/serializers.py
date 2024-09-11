from rest_framework import serializers
from .models import Promotion, Tariff, Product


class PromotionSerializer(serializers.ModelSerializer):
    promo_price = serializers.SerializerMethodField()

    class Meta:
        model = Promotion
        fields = ['name', 'discount_percentage', 'start_date', 'end_date', 'promo_price']

    def get_promo_price(self, obj):
        tariff = self.context.get('tariff')
        if tariff:
            original_price = tariff.price
            discount_percentage = obj.discount_percentage
            return round(original_price * (1 - discount_percentage / 100), 2)
        return None


class TariffSerializer(serializers.ModelSerializer):
    promotions = PromotionSerializer(many=True, read_only=True, context={'tariff': None})

    class Meta:
        model = Tariff
        fields = ['name', 'price', 'promotions']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        context = self.context
        context['tariff'] = instance
        representation['promotions'] = PromotionSerializer(instance.promotions.all(), many=True, context=context).data
        return representation


class ProductSerializer(serializers.ModelSerializer):
    tariffs = TariffSerializer(many=True)

    class Meta:
        model = Product
        fields = ['name', 'tariffs']

