from django.shortcuts import render

from eln.models import Vial
from eln.tables.experiment import ExperimentTable


def vial_details(request, vial_id):
    vial = Vial.objects.prefetch_related("experiments").get(id=vial_id)
    table = ExperimentTable(vial.experiments.all())
    return render(request, "vial_detail.html", {"vial": vial, "table": table})
