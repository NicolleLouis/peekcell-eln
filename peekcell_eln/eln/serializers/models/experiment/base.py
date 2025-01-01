from rest_framework import serializers

from eln.models import Experiment


class ExperimentSerializer(serializers.ModelSerializer):
    vials_label = serializers.SerializerMethodField()

    class Meta:
        model = Experiment
        fields = [
            'id',
            'created_at',
            'experience_type',
            'vials_label',
            'comment',
        ]

    # noinspection PyMethodMayBeStatic
    def get_vials_label(self, obj):
        vials = obj.vial.all()
        return [vial.label for vial in vials]
