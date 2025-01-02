from django.conf import settings
from django.shortcuts import render, redirect
import requests

from eln.forms.vial_sample_creation import VialSampleCreationForm
from eln.tables.vial import VialTable


def vial_sample_creation(request, sample_id):
    if request.method == "POST":
        form = VialSampleCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['storage_id'] = data['storage'].id
            data.pop('storage', None)
            api_url = f"{settings.BASE_URL}/api/samples/{sample_id}/vials/"

            response = requests.post(api_url, json=data)

            if response.status_code == 201:
                created_vials = response.json()
                table = VialTable(created_vials)
                return render(request, "vial_list.html", {"table": table})
            else:
                form.add_error(None, "Failed to create vials.")
    else:
        form = VialSampleCreationForm()

    return render(request, "vial_sample_creation.html", {"form": form})
