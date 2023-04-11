from django import forms

class student_validation(forms.Form):
    faculty = forms.CharField(label="faculty", max_length=30)
    group = forms.CharField(label="group", max_length=10)
    email = forms.CharField(label="email", max_length=100)
