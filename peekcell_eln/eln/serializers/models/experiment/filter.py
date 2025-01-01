from eln.models import ExperimentFilter
from eln.serializers.models.experiment.base import ExperimentSerializer


class ExperimentFilterSerializer(ExperimentSerializer):
    class Meta:
        model = ExperimentFilter
        fields = ExperimentSerializer.Meta.fields + [
            'filter_size',
        ]
