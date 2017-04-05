from django import forms
from characters.models import Location
from .fate_choices import LOCATION_CHOICES

locations = Location.objects.all()
location_choices = ()


# for i in range(0, len(locations)):
#     location_choices


class FateForm(forms.Form):
    test = forms.TextInput()
    your_name = forms.CharField(label='Your name', max_length=100, widget=forms.TextInput())
    # location = forms.ChoiceField(widget=forms.Select(choices=LOCATION_CHOICES))
