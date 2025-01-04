from django.utils.html import format_html
from django_tables2 import tables, SingleTableView, Column

from eln.models import Sample


class SampleTable(tables.Table):
    vial_creation_link = Column(empty_values=(), verbose_name="Create Vials")
    sample_details = Column(empty_values=(), verbose_name="Details")
    last_experiment = Column(empty_values=(), verbose_name="Last Experiment")

    # noinspection PyMethodMayBeStatic
    def render_vial_creation_link(self, record):
        url = f"/eln/samples/{record.id}/vials/create"
        return format_html(
            '<a href="{}" class="btn btn-sm btn-primary">Create</a>',
            url,
        )

    # noinspection PyMethodMayBeStatic
    def render_sample_details(self, record):
        url = f"/eln/samples/{record.id}/"
        return format_html(
            '<a href="{}" class="btn btn-sm btn-primary">Details</a>',
            url,
        )

    # noinspection PyMethodMayBeStatic
    def render_last_experiment(self, record):
        experiments = {experiment for vial in record.vials.all() for experiment in vial.experiments.all()}
        last_experiment = max(
            experiments,
            key=lambda experiment: experiment.created_at,
            default=None
        )
        if last_experiment is None:
            return "Nothing"

        url = f"/eln/api/experiments/{last_experiment.id}/"
        return format_html(
            '<a href="{}">{}</a>',
            url,
            last_experiment.experience_type,
        )

    class Meta:
        model = Sample
        template_name = "django_tables2/bootstrap5.html"
        fields = (
            "label",
            "type",
            "storage",
            "sample_details",
            "vial_creation_link",
        )
        sequence = (
            "label",
            "type",
            "last_experiment",
            "storage",
            "sample_details",
            "vial_creation_link",
        )

class SampleList(SingleTableView):
    model = Sample
    table_class = SampleTable
    template_name = "sample_list.html"
    paginate_by = 20

    def get_queryset(self):
        return Sample.objects.prefetch_related("vials__experiments").all()
