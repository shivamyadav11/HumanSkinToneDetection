from django import forms
from .models import Image_data


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image_data
        fields = ("title", "image")
