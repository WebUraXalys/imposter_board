from django.shortcuts import render, HttpResponse
from .forms import StudentValidation, StudVal
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

def choice_gr(request):
    return render(request, 'board/choice_group.html')

def choice_fac(request):
    if request.method == "POST":
        form = StudentValidation(request.POST)
        if form.is_valid:
            grp = Group.objects.get(name=form.name)
            grp.name = ""
            request.session['group_name'] = grp.name

            user_mail = form.email

            send_mail("Оцінювання викладачів",
            f" Ось ваше особисте посилання для оцінювання викладачів. Воно працює тільки з того девайсу з якого ви відправляти ваші дані. {reverse('main', groupname=grp.name)}",
            settings.DEFAULT_FROM_MAIL, [user_mail])
            
            request.session['allow-group'] = grp.name

    return render(request, 'board/choice_fac.html', context={
        "form": StudentValidation
    })


def serve_main(request, groupname):
    return render(request, 'board/main.html')

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
