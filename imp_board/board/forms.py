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


class TeacherFacCh(forms.Form):
    faculty = forms.ModelChoiceField(queryset=Faculty.objects.all().order_by('name'))


class MarkVal(forms.Form):
    quality = forms.IntegerField(label="quality",min_value=1, max_value=10)
    methodological_support = forms.IntegerField(label="methodological_support",min_value=1, max_value=10)
    objectivity = forms.IntegerField(label="objectivity",min_value=1, max_value=10)
    note = forms.CharField(label="note", min_length=0, max_length=100)
    # def __init__(self, *args, **kwargs):
    #     super(MarkVal, self).__init__(*args, **kwargs)
    #     self.fields['note'].widget.attrs['placeholder'] = 'Додайте кілька слів про викладача та дисипліну'
