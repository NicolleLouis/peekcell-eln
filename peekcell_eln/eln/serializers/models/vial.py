from rest_framework import serializers
from eln.models import Vial


class VialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vial
        fields = ['id', 'storage', 'volume', 'label', 'is_closed', 'is_sediment', 'created_at']
