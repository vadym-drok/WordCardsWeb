from django import forms

from .models import Word

class WordModelForm(forms.ModelForm):
    word = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter new Word"}))
    translation = forms.CharField(
        required=False,

        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter word explanations",
                'class': "taxt_area_form",
                'rows':4,
                'cols': 100,
                }
            )
        )
    class Meta:
        model = Word
        fields = [
            'word',
            'image',
            'translation'
        ]
