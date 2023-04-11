from django.contrib import admin
from .models import Discipline, Mark, Group


# Register your models here.
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher']


class MarkAdmin(admin.ModelAdmin):
    list_display = ['group', 'quality', 'methodological_support', 'objectivity', 'discipline']

class GroupAmin(admin.ModelAdmin):
    list_display = ['name', 'disciplines']


admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Mark, MarkAdmin)
admin.site.register(Group, GroupAmin)
