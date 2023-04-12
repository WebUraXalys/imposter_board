from django.shortcuts import render, HttpResponse, redirect
from django.http.response import JsonResponse
from .forms import StudentValidation, StudVal, TeacherChoice, TeacherFacCh, MarkVal
from .models import *
from django.core.mail import send_mail
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.urls import reverse, reverse_lazy
from datetime import datetime
import xlwt
from xlwt import Workbook
import qrcode
from PIL import Image
import base64
import io

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

            kw = {
                "groupname": grp.name
            }

            send_mail("Оцінювання викладачів",

            f" Ось ваше особисте посилання для оцінювання викладачів. Воно працює тільки з того девайсу з якого ви відправляти ваші дані. http://imp.ig4er.link{reverse('main', kwargs=kw)}",
            settings.DEFAULT_FROM_MAIL, [user_mail])
            
            request.session['allow-group'] = grp.name

            return redirect('mail_sent')

    return render(request, 'board/choice_fac.html', context={
        "form": StudentValidation
    })

def mail_sent(request):
    return render(request, 'board/mail_sent.html')

def create_mark(request):
    if request.method == "POST":
        form = MarkVal(request.POST)

        if form.is_valid():
            q = form.cleaned_data['quality']
            m = form.cleaned_data['methodological_support']
            o = form.cleaned_data['objectivity']
            note = form.cleaned_data['note']

            grp = GroupsToDiscipline.objects.get(id=request.POST.get('gtsid')).group
            disc = GroupsToDiscipline.objects.get(id=request.POST.get('gtsid')).discipline

            semester = current_semester(request, grp.name)

            mrk = Mark.objects.update_or_create(group=grp, quality=int(q), methodological_support=int(m), objectivity=int(o), discipline=disc, semester=semester, note=note)

            # create_or_update_average_mark(mrk)

            return redirect('main', groupname=grp.name)
    else:
        return HttpResponse("405 Method Not Allowed", status=405)

def serve_main(request, groupname):
    if not request.session.get("allow-group", None) == groupname:
        # return PermissionDenied()
        return HttpResponse("403 Forbidden", status=403)
    grp = Group.objects.get(name=groupname)
    context = {

        "disciplines": GroupsToDiscipline.objects.filter(group=grp),
        "form": MarkVal
    }
    print(context['disciplines'])
    return render(request, 'board/main.html', context=context)

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


def group_gen(request):
    fac = Faculty.objects.get(name="Факультет електроніки та комп’ютерних технологій")
    groups = ['ФЕМ', 'ФЕП', 'ФЕС', 'ФЕІ', 'ФЕЛ']
    for i in groups:
        Group.objects.create(name=f"{i}-11", faculty=fac)
    return HttpResponse("Generated")


def tchfc(request):
    if request.method == "POST":
        form = TeacherFacCh(request.POST)
        if form.is_valid():
            fac = form.cleaned_data['faculty']
            return redirect('tch', fac=fac.id)
    return render(request, 'board/teacher_fac.html', context={
        "form": TeacherFacCh
    })

def teacher_ch(request, fac):
    if request.method == "POST":
        form = TeacherChoice(request.POST)
        if form.is_valid():
            print("wdad")
            tn = form.cleaned_data['teacher']
            return redirect('tp', name=tn)
    teachers = Teacher.objects.filter(faculty=Faculty.objects.get(id=fac))
    # tchs = []
    # for t in teachers:
    #     tchs.append(t.name)
    return render(request, 'board/teacher_choice.html', context={
        "teachers": teachers,
        "f": TeacherChoice
    })


def generate_qrcode_to_base64(data):    # Генеруємо QR-код
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Зберігаємо зображення у пам'яті
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    # Конвертуємо зображення до base64
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return image_base64


def teacher_page(request, name):
    teacher = Teacher.objects.get(name=name)
    disciplines = Discipline.objects.filter(teacher=teacher)
    img = generate_qrcode_to_base64('imp/ig4er.link/' + request.get_full_path()[:-1] + "?qr=True")
    data = []
    for discipline in disciplines:
        groups = GroupsToDiscipline.objects.filter(discipline=discipline)
        for group in groups:
            print(group.pk)
            print(discipline.pk)
            avarage = None
            try:
                avarage = AverageMark.objects.get(group=group.pk, discipline=discipline.pk)
            except:
<<<<<<< HEAD
                avarage = None
=======
                average = None
>>>>>>> e9638c9d40f3be107cb19c7d494e33aa491943ca
            stats = {'discipline': discipline,
                     'group': group,
                     'avarage': avarage}
            data.append(stats)
    return render(request, 'board/teacher.html', context={
        "teacher": teacher,
        "data": data,
        "image": img
    })


def create_or_update_average_mark(mark):
    avermark, created = AverageMark.objects.get_or_create(group=mark.group, discipline=mark.discipline, semester=mark.semester)
    if created:
        avermark.quality = mark.quality
        avermark.methodological_support = mark.methodological_support
        avermark.objectivity - mark.objectivity
    else:
        marks_number = len(Mark.objects.filter(group=mark.group, discipline=mark.discipline, semester=mark.semester))
        avermark.quality = (avermark.quality * marks_number) + mark.quality / (marks_number+1)
        avermark.methodological_support = (avermark.methodological_support * marks_number) + mark.methodological_support / (marks_number+1)
        avermark.objectivity = (avermark.objectivity * marks_number) + mark.objectivity / (marks_number+1)
    avermark.save()


def current_semester(request, groupname):
    passed_semesters = (int(groupname[4])-1)*2
    date = datetime.now().month
    if date in range(9, 12):
        semester = 1
    elif date in range(1, 6):
        semester = 2
    else:
        semester = 0

    return semester

def generete_excel(request, pk):
    wb = Workbook()

    group = Group.objects.get(pk=pk)
    disciplines = GroupsToDiscipline.objects.filter(group=pk)
    print(disciplines)
    

    sheet = wb.add_sheet("Sheet 1")

    sheet.write(0, 3, f"Таблиця оцінювання дисциплін групи {group}")
    sheet.write(1, 2, "Примітка:")
    sheet.write(2, 2, "Я: якість викладання, включає зміст навчальної дисципліни, актуальність та структуру матеріалів")
    sheet.write(3, 2, "М: методичне забезпечення — наявність навчальних посібників, конспектів лекцій, презентацій, методичних вказівок, інструкцій до ЛР, індивідуальних завдань тощо.")
    sheet.write(4, 2, "О: об’єктивність оцінювання — включає систему та критерії оцінювання, зокрема розподіл балів протягом семестру та під час екзамену, а також неупередженість та справедливість оцінювання.")

    disc_cell_row = 7
    disc_cell_column = 1
    
    teacher_cell_row = 8
    teacher_cell_column = 1

    head_row=9
    qa_head_column=1
    ms_head_column=2
    ob_head_column=3
    
    qa_cell_column = 1
    ms_cell_column = 2
    ob_cell_column = 3
    note_cell_column = 4

    for discipline in disciplines:
        average = AverageMark.objects.get(group=pk, discipline=discipline.pk)
        sheet.write_merge(disc_cell_row, disc_cell_row, disc_cell_column, disc_cell_column+3, discipline.discipline.name)
        sheet.write_merge(teacher_cell_row, teacher_cell_row, teacher_cell_column, teacher_cell_column+3, discipline.discipline.teacher.name)
        sheet.write(head_row, qa_head_column, f"Сер. Я: {average.quality}")
        sheet.write(head_row, ms_head_column, f"Сер. М: {average.methodological_support}")
        sheet.write(head_row, ob_head_column, f"Сер. О: {average.objectivity}")

        Marks = Mark.objects.filter(group=pk, discipline=discipline.pk)
        cell_row = 10
        n = cell_row-9
        for m in Marks:
            # sheet.write(cell_row, 0, n)
            sheet.write(cell_row, qa_cell_column, m.quality)
            sheet.write(cell_row, ms_cell_column, m.methodological_support)
            sheet.write(cell_row, ob_cell_column, m.objectivity)
            sheet.write(cell_row, note_cell_column, m.note)
            cell_row += 1
            wb.save(f"Оцінювання {group}.xls")


        disc_cell_column += 4
        teacher_cell_column += 4
        qa_head_column += 4
        ms_head_column += 4
        ob_head_column += 4
        qa_cell_column += 4
        ms_cell_column += 4
        ob_cell_column += 4
        note_cell_column += 4

    wb.save(f"Оцінювання {group}.xls")
    return HttpResponse("Generated excel")


def feedbacks(request, name):
    teacher = Teacher.objects.get(name=name)
    disciplines = Discipline.objects.filter(teacher=teacher)
    data = []
    for discipline in disciplines:
        groups = GroupsToDiscipline.objects.filter(discipline=discipline)
        for group in groups:
            try:
                avarage = AverageMark.objects.get(group=group.pk, discipline=discipline.pk).note
            except:
                average = None
            stats = {'discipline': discipline,
                     'group': group,
                     'avarage': avarage}
            data.append(stats)

    return render(request, 'board/teacher.html', context={
        "teacher": teacher,
        "data": data
    })