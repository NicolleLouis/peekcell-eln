from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from eln.models import Experiment, ExperimentFilter, ExperimentCentrifugation, ExperimentQPCR, \
    ExperimentReverseTranscriptase, ExperimentRNAExtraction
from eln.serializers.models.experiment.centrifugation import ExperimentCentrifugationSerializer
from eln.serializers.models.experiment.filter import ExperimentFilterSerializer
from eln.serializers.models.experiment.qPCR import ExperimentQPCRSerializer
from eln.serializers.models.experiment.reverse_transcriptase import ExperimentReverseTranscriptaseSerializer
from eln.serializers.models.experiment.rna_extraction import ExperimentRNAExtractionSerializer


class ExperimentDetailView(APIView):
    def get(self, request, experiment_id):
        try:
            experiment = Experiment.objects.get(id=experiment_id).get_instance_subclass()
            serializer_class = self.get_serializer_class(experiment)
            serializer = serializer_class(experiment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Experiment.DoesNotExist:
            return Response({"error": "Experiment not found"}, status=status.HTTP_404_NOT_FOUND)

    def get_serializer_class(self, instance):
        match instance:
            case ExperimentFilter():
                return ExperimentFilterSerializer
            case ExperimentCentrifugation():
                return ExperimentCentrifugationSerializer
            case ExperimentQPCR():
                return ExperimentQPCRSerializer
            case ExperimentReverseTranscriptase():
                return ExperimentReverseTranscriptaseSerializer
            case ExperimentRNAExtraction():
                return ExperimentRNAExtractionSerializer
            case _:
                raise NotImplementedError(f"{type(instance.get_instance_subclass())} has no serializer yet")
