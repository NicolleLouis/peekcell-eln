from eln.models import ExperimentReverseTranscriptase
from eln.serializers.models.experiment.base import ExperimentSerializer


class ExperimentReverseTranscriptaseSerializer(ExperimentSerializer):
    class Meta:
        model = ExperimentReverseTranscriptase
        fields = ExperimentSerializer.Meta.fields + [
            'kit',
            'rna_dilution',
            'dilution_rna_volume',
            'dilution_water_volume',
            'input_volume',
            'contain_spike_in',
        ]
