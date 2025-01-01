from django_tables2 import tables, SingleTableView

from eln.models import Experiment

class ExperimentTable(tables.Table):
    vial_labels = tables.Column(accessor='get_vial_labels', verbose_name="Vials")
    readable_created_at = tables.Column(verbose_name="Date")

    class Meta:
        model = Experiment
        template_name = "django_tables2/bootstrap5.html"
        fields = (
            "readable_created_at",
            "experience_type",
        )
        sequence = (
            "readable_created_at",
            "experience_type",
            "vial_labels",
        )


class ExperimentList(SingleTableView):
    model = Experiment
    table_class = ExperimentTable
    template_name = "experiment_list.html"
    paginate_by = 20

    def get_queryset(self):
        return Experiment.objects.prefetch_related("vial").order_by("-created_at")
