from rest_framework.views import APIView
from rest_framework.response import Response

from eln.models import ProductName
from eln.models.analytic.product import ProductAnalytics
from eln.serializers.analytics.product import ProductAnalyticSerializer


class ProductAnalyticView(APIView):
    def get(self, request):
        data = []
        for product_key, product_label in ProductName.choices:
            data.append(ProductAnalytics(product_key, product_label))
        serializer = ProductAnalyticSerializer(data, many=True)
        return Response(serializer.data)
