from django import forms
from .models import *


class ImageUploadForm(forms.ModelForm):
    event_all_images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}), required=True)

    class Meta:
        model = Event
        fields = ["event_name", "event_cover", "date", "details"]
