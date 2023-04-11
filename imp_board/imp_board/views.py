from django.shortcuts import render, HttpResponse

def choice_group(request):
    return render(request, 'imp_board/index.html')
