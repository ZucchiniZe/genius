from django import forms
from taggit.forms import TagField

from .models import Peak


class PeakForm(forms.ModelForm):
    tags = TagField(label='Tags (comma separated list of tags)', required=False)
    description = forms.CharField(label='Body', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))

    class Meta:
        model = Peak
        fields = ['title', 'description', 'tags', 'private']
        exclude = ('user', 'pub_date')
