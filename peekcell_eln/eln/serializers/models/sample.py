from rest_framework import serializers
from eln.models import Sample
from eln.serializers.models.vial import VialSerializer


class SampleSerializer(serializers.ModelSerializer):
    vials = VialSerializer(many=True, read_only=True)

    class Meta:
        model = Sample
        fields = ['id', 'storage', 'type', 'vials']
