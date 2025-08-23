# weather_app/forms.py

from django import forms

class CityForm(forms.Form):
    """A simple form to get the city name from the user."""
    name = forms.CharField(label='City Name', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter a City'}))