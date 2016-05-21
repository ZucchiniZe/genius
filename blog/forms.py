from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    body = forms.CharField(label='Body', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))

    class Meta:
        model = Post
        exclude = ('pub_date', 'author')
