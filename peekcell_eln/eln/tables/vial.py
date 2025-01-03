from django.utils.html import format_html
from django_tables2 import tables, Column

from eln.models import Vial


class VialTable(tables.Table):
    vial_details = Column(empty_values=(), verbose_name="Details")

    # noinspection PyMethodMayBeStatic
    def render_vial_details(self, record):
        url = f"/eln/vials/{record.id}/"
        return format_html(
            '<a href="{}" class="btn btn-sm btn-primary">Details</a>',
            url,
        )

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
