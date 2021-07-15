from django import forms
from .models import ApiCall

class ApiCallForm(forms.ModelForm):
    class Meta:
        model = ApiCall
        fields = '__all__'