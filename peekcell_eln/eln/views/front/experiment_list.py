from django.utils.html import format_html
from django_tables2 import tables, SingleTableView, A, Column
from django_tables2.columns import LinkColumn

from eln.models import Experiment


class ExperimentTable(tables.Table):
    vial_labels = tables.Column(accessor='get_vial_labels', verbose_name="Vials")
    readable_created_at = tables.Column(verbose_name="Date")
    custom_link = Column(empty_values=(), verbose_name="Details")

    # noinspection PyMethodMayBeStatic
    def render_custom_link(self, record):
        url = f"/eln/api/experiments/{record.id}/"
        return format_html(
            '<a href="{}">View</a>',
            url,
        )

    class Meta:
        model = Experiment
        template_name = "django_tables2/bootstrap5.html"
        fields = (
            "readable_created_at",
            "experience_type",
            "custom_link",
        )
        sequence = (
            "readable_created_at",
            "experience_type",
            "vial_labels",
            "custom_link",
        )


class ExperimentList(SingleTableView):
    model = Experiment
    table_class = ExperimentTable
    template_name = "experiment_list.html"
    paginate_by = 20

    def get_queryset(self):
        return Experiment.objects.prefetch_related("vial").order_by("-created_at")
