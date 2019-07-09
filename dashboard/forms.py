from django import forms
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['category', 'blogger', 'url', 'title', 'image', 'content']

    def __init__(self, data = None,*args, **kwargs):
        super().__init__(data = data,*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20,widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))