from django.contrib import admin
from .models import Discipline, Mark


# Register your models here.
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher']
    


class MarkAdmin(admin.ModelAdmin):
    list_display = ['group', 'quality', 'methodological_support', 'objectivity', 'discipline']


class AverageMarkAdmin(admin.ModelAdmin):
    list_display = ['group', 'quality', 'methodological_support', 'objectivity', 'discipline']


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Mark, MarkAdmin)