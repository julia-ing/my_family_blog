from django import forms
from .models import myText

class LectureForm(forms.ModelForm):
    class Meta:
        model = myText
        fields = (
            'author',
            'title',
            'img_url',
            'category',
            'board_text',
        )