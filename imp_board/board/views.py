from django.shortcuts import render, HttpResponse

# Create your views here.

def choice_gr(request):
    return render(request, 'board/inedx.html')