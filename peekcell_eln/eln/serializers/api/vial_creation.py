from rest_framework import serializers


class VialCreationSerializer(serializers.Serializer):
    number = serializers.IntegerField(min_value=1)
    volume = serializers.IntegerField(min_value=1)
    storage_id = serializers.IntegerField()
