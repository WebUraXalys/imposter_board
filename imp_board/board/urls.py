from django.urls import path
from .views import *

urlpatterns = [
    path('', choice_gr, name=""),
]
