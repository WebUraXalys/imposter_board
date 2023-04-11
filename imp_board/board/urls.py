from django.urls import path
from .views import *

urlpatterns = [
    path('', choice_gr, name="choice"),
    path('student/', choice_fac, name="choice_fac"),
    path('email/', send_invitation, name="email"),
    path('mark/<groupname>', serve_main, name="main"),
    path('facgen/', generate_faculties, name="facgen"),
    path('groupgen/', group_gen, name="groupgen")
]
