from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label="Search for a movie", max_length=100)
    # page = forms.IntegerField(label='Page', min_value=1, required=False)
