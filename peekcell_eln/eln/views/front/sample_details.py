from django.shortcuts import render

from eln.models import Sample
from eln.tables.vial import VialTable


def sample_details(request, sample_id):
    sample = Sample.objects.prefetch_related("vials__experiments").get(id=sample_id)
    samples = sample.vials
    open_samples = samples.filter(is_closed=False)
    table = VialTable(open_samples)
    return render(request, "sample_detail.html", {"sample": sample, "table": table})
