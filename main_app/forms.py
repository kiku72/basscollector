from django.forms import ModelForm
from .models import Strings

class StringForm(ModelForm):
    class Meta:
        model = Strings
        fields = ['make', 'model', 'variety']