from django_tables2 import SingleTableView

from eln.models import Experiment
from eln.tables.experiment import ExperimentTable


class ExperimentList(SingleTableView):
    model = Experiment
    table_class = ExperimentTable
    template_name = "experiment_list.html"
    paginate_by = 20

    def get_queryset(self):
        return Experiment.objects.prefetch_related("vial").order_by("-created_at")
