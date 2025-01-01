from eln.models import ExperimentRNAExtraction
from eln.serializers.models.experiment.base import ExperimentSerializer


class ExperimentRNAExtractionSerializer(ExperimentSerializer):
    class Meta:
        model = ExperimentRNAExtraction
        fields = ExperimentSerializer.Meta.fields + [
            'kit',
            'input_volume',
            'elution_volume',
            'contain_spike_in',
        ]
