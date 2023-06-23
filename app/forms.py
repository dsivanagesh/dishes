from django import forms

class SearchForm(forms.Form):
    dish_name = forms.CharField(max_length=255, label='Search')