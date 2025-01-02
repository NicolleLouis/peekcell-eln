from django import forms

from eln.models import Storage


class VialSampleCreationForm(forms.Form):
    number = forms.IntegerField(label="Number", min_value=1)
    volume = forms.FloatField(label="Volume", min_value=0)
    storage = forms.ModelChoiceField(
        label="Storage",
        queryset=Storage.objects.all(),
        empty_label="Select a storage",
        error_messages={"required": "Please select a valid storage."},
    )
