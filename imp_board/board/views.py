from django.shortcuts import render, HttpResponse
from .forms import StudentValidation
from .models import *
from django.core.mail import send_mail

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
        "from": StudentValidation
    })


def send_invitation(request):
    send_mail(
        'Запрошення до оціцнювання',
        'Вітаємо. Це тестове повідомлення для перевірки роботи',
        'volodymyrpetriv2207@gmail.com',
        ['volodymyrpetriv2207@gmail.com'],
    )
