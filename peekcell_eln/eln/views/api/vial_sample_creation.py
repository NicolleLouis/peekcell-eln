from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db import transaction

from eln.models import Sample, Vial, Storage
from eln.serializers.api.vial_creation import VialCreationSerializer
from eln.serializers.models.vial import VialSerializer
from eln.services.alphabetical import AlphabeticalService


class VialSampleCreateView(APIView):
    serializer_class = VialCreationSerializer

    @extend_schema(
        request=VialCreationSerializer,
        responses=VialSerializer,
    )
    def post(self, request, sample_id):
        serializer = VialCreationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        try:
            sample = Sample.objects.get(id=sample_id)
        except Sample.DoesNotExist:
            return Response({"detail": "Sample not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            storage = Storage.objects.get(id=data['storage_id'])
        except Storage.DoesNotExist:
            return Response({"detail": "Storage not found"}, status=status.HTTP_404_NOT_FOUND)

        with transaction.atomic():
            vials = [
                Vial(
                    label=f"{sample.label}{AlphabeticalService.int_to_capital_letter(index)}",
                    sample=sample,
                    volume=data['volume'],
                    storage=storage,
                    is_sediment=data['is_sediment'],
                )
                for index in range(data['number'])
            ]
            vials = Vial.objects.bulk_create(vials)

        return Response(
            VialSerializer(vials, many=True).data,
            status=status.HTTP_201_CREATED
        )
