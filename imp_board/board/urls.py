from django.urls import path
from .views import *

urlpatterns = [
    path('', choice_gr, name="choice"),
    path('student/', choice_fac, name="choice_fac")
]
