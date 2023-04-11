from django.shortcuts import render, HttpResponse
from .forms import student_validation

# Create your views here.

def choice_gr(request):
    return render(request, 'board/choice_group.html', context={
        "form": student_validation
    })
