from django.contrib import admin
from .models import Discipline, Mark, Teacher, Faculty, Group, AverageMark, GroupsToDiscipline


# Register your models here.
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name']


class DisciplineAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher']
    

class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'disciplines', 'faculty']

    def get_disciplines(self, obj):
        return [discipline.name for discipline in obj.discipline.all()]


class MarkAdmin(admin.ModelAdmin):
    list_display = ['group', 'quality', 'methodological_support', 'objectivity', 'discipline']


class AverageMarkAdmin(admin.ModelAdmin):
    list_display = ['group', 'quality', 'methodological_support', 'objectivity', 'discipline']

class GroupsToDisciplineAdmin(admin.ModelAdmin):
    list_display = ['discipline', 'group']


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Mark, MarkAdmin)
admin.site.register(AverageMark, AverageMarkAdmin)
admin.site.register(GroupsToDiscipline, GroupsToDisciplineAdmin)
