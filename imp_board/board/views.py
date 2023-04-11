from django.shortcuts import render, HttpResponse
from .forms import student_validation
from django.core.mail import send_mail

# Create your views here.

def choice_gr(request):
    return render(request, 'board/choice_group.html')

def choice_fac(request):
    return render(request, 'board/choice_fac.html', context={
<<<<<<< Updated upstream
        "form": student_validation
    })
=======
        "from": student_validation
    })


def send_invitation(request):
    send_mail(
        'Запрошення до оціцнювання',
        'Вітаємо. Це тестове повідомлення для перевірки роботи',
        'volodymyrpetriv2207@gmail.com',
        ['volodymyrpetriv2207@gmail.com'],
    )
>>>>>>> Stashed changes
