from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from eln.models import Experiment
from eln.serializers.models.experiment import ExperimentSerializer


class ExperimentView(APIView):
    def get(self, request):
        experiments = Experiment.objects.all()
        serializer = ExperimentSerializer(experiments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
