from django import forms
from .models import Group

class StudVal(forms.ModelForm):
    faculty = forms.CharField(label="faculty", max_length=30)
    group = forms.CharField(label="group", max_length=10)

    class Meta:
        model = Group
        fields = ['name']


class StudentValidation(forms.Form):
    faculty = forms.CharField(label="faculty", max_length=30)
    # group = forms.CharField(label="group", max_length=10)
    group = forms.ModelChoiceField(queryset=Group.objects.all().order_by('name'))
    email = forms.CharField(label="email", max_length=100)
