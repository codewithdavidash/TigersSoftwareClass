from django import forms
from comment.models import *

INPUT_STYLES = """
padding: 5px;
height: 150px;
border: 2px solid transparent;
"""

class HTMLCommentForm(forms.ModelForm):
     class Meta:
          model = HTMLComments
          fields = ('name', 'comment',)
     name = forms.CharField(widget=forms.TextInput(attrs={
          'placeholder': 'Username...',
          'style': 'width: 270px; height: 30px; border-radius: 2px; border: 2px solid transparent;'
     }))
     comment = forms.CharField(widget=forms.Textarea(attrs={
          'placeholder': 'Add a comment...',
          'style': INPUT_STYLES
     }))

class CSSCommentForm(forms.ModelForm):
     class Meta:
          model = CSSComments
          fields = ('name', 'comment',)
     name = forms.CharField(widget=forms.TextInput(attrs={
          'placeholder': 'Username...',
          'style': 'width: 270px; height: 30px; border-radius: 2px; border: 2px solid transparent;'
     }))
     comment = forms.CharField(widget=forms.Textarea(attrs={
          'placeholder': 'Add a comment...',
          'style': INPUT_STYLES
     }))

class JSCommentForm(forms.ModelForm):
     class Meta:
          model = JSComments
          fields = ('name', 'comment',)
     name = forms.CharField(widget=forms.TextInput(attrs={
          'placeholder': 'Username...',
          'style': 'width: 270px; height: 30px; border-radius: 2px; border: 2px solid transparent;'
     }))
     comment = forms.CharField(widget=forms.Textarea(attrs={
          'placeholder': 'Add a comment...',
          'style': INPUT_STYLES
     }))

class PYTHONCommentForm(forms.ModelForm):
     class Meta:
          model = PythonComments
          fields = ('name', 'comment',)
     name = forms.CharField(widget=forms.TextInput(attrs={
          'placeholder': 'Username...',
          'style': 'width: 270px; height: 30px; border-radius: 2px; border: 2px solid transparent;'
     }))
     comment = forms.CharField(widget=forms.Textarea(attrs={
          'placeholder': 'Add a comment...',
          'style': INPUT_STYLES
     }))