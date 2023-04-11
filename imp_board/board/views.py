from django.shortcuts import render, HttpResponse
from .forms import StudentValidation, StudVal
from .models import *
from django.core.mail import send_mail
from django.conf import settings

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


def send_invitation(request):
    print(settings.EMAIL_HOST_USER)
    print(settings.EMAIL_HOST_PASSWORD)
    send_mail(
        'Invitation',
        'Вітаємо. Це тестове повідомлення для перевірки роботи',
        'volodymyrpetriv2207@gmail.com',
        recipient_list=['etrikodoku@gmail.com'],
        fail_silently=False
    )
    return HttpResponse("Sent")
