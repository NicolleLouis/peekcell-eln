from rest_framework import serializers

from eln.models import ExperimentQPCR
from eln.serializers.models.experiment.base import ExperimentSerializer


class ExperimentQPCRSerializer(ExperimentSerializer):
    primers_label = serializers.SerializerMethodField()

    class Meta:
        model = ExperimentQPCR
        fields = ExperimentSerializer.Meta.fields + [
            'primers_label',
        ]

    # noinspection PyMethodMayBeStatic
    def get_primers_label(self, obj):
        primers = obj.primer.all()
        return [primer.name for primer in primers]
