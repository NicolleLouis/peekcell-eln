from eln.models import ExperimentCentrifugation
from eln.serializers.models.experiment.base import ExperimentSerializer


class ExperimentCentrifugationSerializer(ExperimentSerializer):
    class Meta:
        model = ExperimentCentrifugation
        fields = ExperimentSerializer.Meta.fields + [
            'speed',
            'duration',
            'temperature',
        ]
