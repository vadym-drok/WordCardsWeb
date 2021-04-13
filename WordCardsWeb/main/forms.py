from django import forms

from .models import Word

class WordModelForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = [
            'word',
            'image',
            'translation'
        ]
