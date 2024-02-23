from django import forms
from demo.models import sam

class samform(forms.ModelForm):
    class Meta:
        model=sam
        fields="__all__"