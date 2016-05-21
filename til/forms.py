from django import forms
from taggit.forms import TagField

from .models import TIL


class TilForm(forms.ModelForm):
    tags = TagField(label='Tags (comma separated list of tags)')
    description = forms.CharField(label='Body', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))

    class Meta:
        model = TIL
        fields = ['title', 'description', 'tags', 'private']
        exclude = ('user', 'pub_date')
