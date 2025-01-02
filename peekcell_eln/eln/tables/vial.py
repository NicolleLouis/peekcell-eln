from django_tables2 import tables

from eln.models import Vial


class VialTable(tables.Table):
    class Meta:
        model = Vial
        template_name = "django_tables2/bootstrap5.html"
        fields = (
            "label",
            "volume",
            "is_closed",
            "is_sediment",
            "storage",
        )
