from django import forms
from taggit.forms import TagField


class TilForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Body', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
    tags = TagField(label='Tags (comma separated list of tags)')
    private = forms.BooleanField(label='Private?', required=False)
