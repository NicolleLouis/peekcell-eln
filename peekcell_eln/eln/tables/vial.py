from django.utils.html import format_html
from django_tables2 import tables, Column

from eln.models import Vial


class VialTable(tables.Table):
    vial_details = Column(empty_values=(), verbose_name="Details")
    last_experiment = Column(empty_values=(), verbose_name="Last Experiment")

    # noinspection PyMethodMayBeStatic
    def render_vial_details(self, record):
        url = f"/eln/vials/{record.id}/"
        return format_html(
            '<a href="{}" class="btn btn-sm btn-primary">Details</a>',
            url,
        )

    # noinspection PyMethodMayBeStatic
    def render_last_experiment(self, record):
        last_experiment = record.experiments.order_by('-created_at').first()
        if not last_experiment:
            return "Nothing"

        url = f"/eln/api/experiments/{last_experiment.id}/"
        return format_html(
            '<a href="{}">{}</a>',
            url,
            last_experiment.experience_type,
        )

    class Meta:
        model = Vial
        template_name = "django_tables2/bootstrap5.html"
        fields = (
            "label",
            "volume",
            "is_sediment",
            "storage",
        )
        sequence = (
            "label",
            "is_sediment",
            "last_experiment",
            "volume",
            "storage",
            "vial_details",
        )
