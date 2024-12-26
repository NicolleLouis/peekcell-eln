from rest_framework import serializers

from eln.models import Person
from eln.serializers.models.sample import SampleSerializer


class PersonSerializer(serializers.ModelSerializer):
    samples = SampleSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = [
            'id',
            'first_name',
            'last_name',
            'hospital',
            'clinical_study',
            'is_test',
            'samples'
        ]
