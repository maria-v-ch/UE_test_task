from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_xml.renderers import XMLRenderer
from django.utils import timezone
from .models import Product
from .serializers import ProductSerializer, TariffSerializer


class ProductTariffView(APIView):
    renderer_classes = [XMLRenderer]

    def get(self, request):
        current_date = timezone.now().date()
        products = Product.objects.prefetch_related('tariffs__promotions').all()

        serializer = ProductSerializer(products, many=True)
        data = serializer.data

        for product in data:
            for tariff in product['tariffs']:
                promotions = tariff.get('promotions', [])
                valid_promotions = [p for p in promotions if p['start_date'] <= str(current_date) <= p['end_date']]
                valid_promotions.sort(key=lambda x: x['discount_percentage'], reverse=True)
                tariff['promotions'] = valid_promotions

        return Response(data)
