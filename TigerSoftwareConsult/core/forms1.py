from django import forms
from comment.models import *


INPUT_STYLES = """
padding: 5px;
height: 40px;
"""

class HTMLForm(forms.ModelForm):
     class Meta:
          model = HTML
          fields = ('name', 'video_link', 'notes')
     name = forms.CharField(widget=forms.TextInput(attrs={
          'placeholder': 'The name of your video...',
          'style': INPUT_STYLES
     }))
     video_link = forms.CharField(widget=forms.URLInput(attrs={
          'placeholder': 'Your video_link...',
          'style': INPUT_STYLES
     }))

class CSSForm(forms.ModelForm):
     class Meta:
          model = CSS
          fields = ('name', 'video_link', 'notes')
     name = forms.CharField(widget=forms.TextInput(attrs={
          'placeholder': 'The name of your course...',
          'style': INPUT_STYLES
     }))
     video_link = forms.CharField(widget=forms.URLInput(attrs={
          'placeholder': 'Your video_link...',
          'style': INPUT_STYLES
     }))

class JSForm(forms.ModelForm):
     class Meta:
          model = JAVASCRIPT
          fields = ('name', 'video_link', 'notes')
     name = forms.CharField(widget=forms.TextInput(attrs={
          'placeholder': 'The name of your course...',
          'style': INPUT_STYLES
     }))
     video_link = forms.CharField(widget=forms.URLInput(attrs={
          'placeholder': 'Your video_link...',
          'style': INPUT_STYLES
     }))

class PYTHONForm(forms.ModelForm):
     class Meta:
          model = PYTHON
          fields = ('name', 'video_link', 'notes')
     name = forms.CharField(widget=forms.TextInput(attrs={
          'placeholder': 'The name of your course...',
          'style': INPUT_STYLES
     }))
     video_link = forms.CharField(widget=forms.URLInput(attrs={
          'placeholder': 'Your video_link...',
          'style': INPUT_STYLES
     }))
