from rest_framework import serializers


class VialCreationSerializer(serializers.Serializer):
    number = serializers.IntegerField(min_value=1)
    volume = serializers.IntegerField(min_value=1)
    is_sediment = serializers.BooleanField(default=False)
    storage_id = serializers.IntegerField()
