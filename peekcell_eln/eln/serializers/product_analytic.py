from rest_framework import serializers

class ProductAnalyticSerializer(serializers.Serializer):
    product_label = serializers.CharField()
    has_one_opened = serializers.BooleanField()
    number_in_stock = serializers.IntegerField()
