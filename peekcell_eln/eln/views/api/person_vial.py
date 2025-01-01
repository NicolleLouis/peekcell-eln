from rest_framework.generics import RetrieveAPIView

from eln.models import Person
from eln.serializers.models.person import PersonSerializer


class PersonVialView(RetrieveAPIView):
    queryset = Person.objects.prefetch_related('samples__vials')
    serializer_class = PersonSerializer
