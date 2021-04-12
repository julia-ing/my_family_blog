from django import forms
from .models import myText

class PostingForm(forms.ModelForm):
    class Meta:
        model = myText
        fields = (
            'author',
            'title',
            'img_url',
            'category',
            'board_text',
        )