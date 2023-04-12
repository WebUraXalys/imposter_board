from django.urls import path
from .views import *

urlpatterns = [
    path('', choice_gr, name="choice"),
    path('student/', choice_fac, name="choice_fac"),
    path('email/', send_invitation, name="email"),
    path('mark/<groupname>', serve_main, name="main"),
    path('facgen/', generate_faculties, name="facgen"),
    path('groupgen/', group_gen, name="groupgen"),
    path('curr_semester/<pk>', current_semester, name="semester"),
    path('mail_sent/', mail_sent, name="mail_sent"),
    path('addmark/', create_mark, name="addmark"),
    path("gen/<pk>", generete_excel),
    path('tcf/', tchfc, name="tchfc"),
    path('tc/<int:fac>', teacher_ch, name="tch"),
    path('t/<name>/', teacher_page, name="tp")
]
