from django.shortcuts import render, HttpResponse, redirect
from .forms import StudentValidation
from .models import *

# Create your views here.

def choice_gr(request):
    return render(request, 'board/choice_group.html')

def choice_fac(request):
    if request.method == "POST":
        form = StudentValidation(request.POST)
        if form.is_valid:
                grp = Group.objects.get(name=form.name)
                request.session['group_name'] = grp.name
    return render(request, 'board/choice_fac.html', context={
        "form": StudentValidation
    })