from django import forms
from .models import Mclass1, teacher

class Sform(forms.Form):
    name = forms.CharField(max_length = 50)
    email  = forms.EmailField()
    zipcode = forms.CharField(max_length = 50)

class Mform(forms.ModelForm):
    class Meta:
        model = Mclass1
        fields = "__all__"

class Mteacher(forms.ModelForm):
    class Meta:
        model = teacher
        fields = "__all__"
