from django import forms
from .models import Group, Faculty, Teacher

class StudVal(forms.ModelForm):
    faculty = forms.CharField(label="faculty", max_length=30)
    group = forms.CharField(label="group", max_length=10)

    class Meta:
        model = Group
        fields = ['name']


class StudentValidation(forms.Form):
    faculty = forms.ModelChoiceField(queryset=Faculty.objects.all().order_by('name'))
    # faculty = forms.CharField(label="faculty", max_length=30)
    # group = forms.CharField(label="group", max_length=10)
    group = forms.ModelChoiceField(queryset=Group.objects.all().order_by('name'))
    email = forms.CharField(label="email", max_length=100)

    def __init__(self, *args, **kwargs):
        super(StudentValidation, self).__init__(*args, **kwargs)
        self.fields['faculty'].widget.attrs['placeholder'] = 'Оберіть ваш факультет'
        self.fields['group'].widget.attrs['placeholder'] = 'Оберіть вашу групу'
        self.fields['email'].widget.attrs['placeholder'] = 'Вкажіть свою корпоративну пошту'

class TeacherChoice(forms.Form):
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all().order_by('name'))
