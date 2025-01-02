from django.utils.html import format_html
from django_tables2 import tables, SingleTableView, Column

from eln.models import Sample


class SampleTable(tables.Table):
    vial_creation_link = Column(empty_values=(), verbose_name="Create Vials")

    # noinspection PyMethodMayBeStatic
    def render_vial_creation_link(self, record):
        url = f"/eln/samples/{record.id}/vials/create"
        return format_html(
            '<a href="{}" class="btn btn-sm btn-primary">Create</a>',
            url,
        )

    class Meta:
        model = Sample
        template_name = "django_tables2/bootstrap5.html"
        fields = (
            "label",
            "type",
            "storage",
            "vial_creation_link",
        )

class SampleList(SingleTableView):
    model = Sample
    table_class = SampleTable
    template_name = "sample_list.html"
    paginate_by = 20

    def get_queryset(self):
        return Sample.objects.all()
