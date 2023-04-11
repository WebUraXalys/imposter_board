from django.shortcuts import render, HttpResponse, redirect
from .forms import StudentValidation, StudVal
from .models import *
from django.core.mail import send_mail
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.urls import reverse, reverse_lazy

def choice_gr(request):
    return render(request, 'board/choice_group.html')

def choice_fac(request):
    if request.method == "POST":
        form = StudentValidation(request.POST)
        if form.is_valid():
            grp = form.cleaned_data['group']
            request.session['group_name'] = grp.name

            user_mail = form.cleaned_data['email']
            if not user_mail.endswith("@lnu.edu.ua") and settings.DEBUG == False:
                return HttpResponse('403 Forbidden', status=403)

            send_mail("Оцінювання викладачів",
 
            f" Ось ваше особисте посилання для оцінювання викладачів. Воно працює тільки з того девайсу з якого ви відправляти ваші дані. {reverse('main', groupname=grp.name)}",
            settings.DEFAULT_FROM_MAIL, [user_mail])
            
            request.session['allow-group'] = grp.name

    return render(request, 'board/choice_fac.html', context={
        "form": StudentValidation
    })


def serve_main(request, groupname):
    if not request.session.get("allow-group", None) == groupname:
        # return PermissionDenied()
        return HttpResponse("403 Forbidden", status=403)
    grp = Group.objects.get(name=groupname)
    context = {

        "disciplines": grp.disciplines.all()
    }
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


def generate_faculties(request):
    faculties = ['Біологічний факультет',
                 'Географічний факультет',
                 'Геологічний факультет',
                 'Економічний факультет',
                 'Факультет електроніки та комп’ютерних технологій',
                 'Факультет журналістики',
                 'Факультет іноземних мов',
                 'Історичний факультет',
                 'Факультет культури і мистецтв',
                 'Механіко-математичний факультет',
                 'Факультет міжнародних відносин',
                 'Факультет педагогічної освіти',
                 'Факультет прикладної математики та інформатики',
                 'Факультет управління фінансами та бізнесу',
                 'Фізичний факультет',
                 'Філологічний факультет',
                 'Філософський факультет',
                 'Хімічний факультет',
                 'Юридичний факультет']
    
    for faculty in faculties:
        Faculty.objects.create(name=faculty)
    return HttpResponse("Done")