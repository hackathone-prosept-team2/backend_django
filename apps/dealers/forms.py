from django import forms

from .crud import list_dealers
from .models import Match

STATUS_CHOICES = [("", "---------")] + Match.MatchStatus.choices


class FilterForm(forms.Form):
    text = forms.CharField(required=False)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)
    dealer = forms.ModelChoiceField(queryset=list_dealers(), required=False)
