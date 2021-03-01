from django.forms import ModelForm
from django import forms
from talk.models import Talk, Comment
from django.utils.translation import gettext_lazy as _

class TalkForm(ModelForm):
    class Meta:
        model = Talk
        fields = ['content', 'password', 'writer']
        labels = {
            'content': _('사랑의 한마디'),
            'writer': _('작성자'),
            'password': _('작성자 비밀번호'),
        }
        widgets = {
            'password': forms.PasswordInput()
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'talk', 'writer']
        labels = {
            'writer': _('작성자'),
            'content': _('코멘트'),
        }
        widgets = {
            'talk': forms.HiddenInput()
        }

class UpdateTalkForm(TalkForm):
    class Meta:
        model = Talk
        exclude = ['password']
