from django.db import models
from django import forms
from .models import *

cities = (
    (None, '--'),
    ('Los Angeles', 'Los Angeles'),
    ('Atlanta', 'Atlanta'),
    ('Austin', 'Austin'),
    ('Boston', 'Boston'),
    ('Chicago', 'Chicago'),
    ('Dallas', 'Dallas'),
    ('Denver', 'Denver'),
    ('Detroit', 'Detroit'),
    ('Houston', 'Houston'),
    ('Las Vegas', 'Las Vegas'),
    ('Los Angeles', 'Los Angeles'),
    ('Miami', 'Miami'),
    ('Minneapolis', 'Minneapolis'),
    ('New York', 'New York'),
    ('Orange County', 'Orange County'),
    ('Philadelphia', 'Philadelphia'),
    ('Phoenix','Phoenix'),
    ('Portland','Portland'),
    ('Raleigh','Raleigh'),
    ('Sacramento','Sacramento'),
    ('San Antonio', 'San Antonio'),
    ('San Diego','San Diego'),
    ('Seattle','Seattle'),
    ('SF Bay Area', 'SF Bay'),
    ('Washington DC', 'Washington DC')
)

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.ChoiceField(choices=cities)
