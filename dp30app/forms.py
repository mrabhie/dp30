from django import forms
from dp30app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields="__all__"

class WebpageForm(forms.ModelForm):
    class Meta:
        model=WebPage
        fields=("topic","name","url")#"__all__"
        exclude=("url",)