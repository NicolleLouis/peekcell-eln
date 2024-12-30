from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db import transaction

from eln.models import Vial, Storage
from eln.serializers.api.vial_creation import VialCreationSerializer
from eln.serializers.models.vial import VialSerializer


class VialSplittingCreateView(APIView):
    serializer_class = VialCreationSerializer

    @extend_schema(
        request=VialCreationSerializer,
        responses=VialSerializer,
    )
    def post(self, request, vial_id):
        serializer = VialCreationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        try:
            vial = Vial.objects.get(id=vial_id)
        except Vial.DoesNotExist:
            return Response({"detail": "Vial not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            storage = Storage.objects.get(id=data['storage_id'])
        except Storage.DoesNotExist:
            return Response({"detail": "Storage not found"}, status=status.HTTP_404_NOT_FOUND)

        if not self.can_be_split(vial=vial, data=data):
            return Response(
                {"detail": "Cannot split vial, not enough volume"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        vials = self.create_vials(
            vial=vial,
            storage=storage,
            data=data,
        )

        self.update_vial(vial, data)

        return Response(
            VialSerializer(vials, many=True).data,
            status=status.HTTP_201_CREATED,
            )

    @staticmethod
    def create_vials(vial, storage, data):
        with transaction.atomic():
            vials = [
                Vial(
                    label=f"{vial.label}.{index + 1}",
                    sample=vial.sample,
                    volume=data['volume'],
                    storage=storage,
                    is_sediment=data['is_sediment'],
                )
                for index in range(data['number'])
            ]
            vials = Vial.objects.bulk_create(vials)

        for _vial in vials:
            _vial.experiments.set(vial.experiments.all())

        return vials

    @staticmethod
    def can_be_split(vial, data):
        return data['number'] * data['volume'] <= vial.volume

    @staticmethod
    def remaining_volume(vial, data):
        return vial.volume - data['number'] * data['volume']

    def update_vial(self, vial, data):
        remaining_volume = self.remaining_volume(vial, data)
        if remaining_volume == 0:
            vial.delete()
            return
        else:
            vial.volume = remaining_volume
            vial.label = f"{vial.label}.0"
            vial.save()
            return vial