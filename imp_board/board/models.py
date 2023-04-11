from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=40, verbose_name="Faculty name")
    
    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=20, verbose_name="Teacher name")
    
    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length=20, verbose_name="Discipline name")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=6, verbose_name="Group name")
    disciplines = models.ManyToManyField(Discipline, blank=True),
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class GroupsToDiscipline(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.discipline + " " + self.group

class Mark(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    quality = models.IntegerField(default=5, validators=[MaxValueValidator(10),
                                                        MinValueValidator(1)])
    methodological_support = models.IntegerField(default=5, validators=[MaxValueValidator(10),
                                                                       MinValueValidator(1)])
    objectivity = models.IntegerField(default=5, validators=[MaxValueValidator(10),
                                                            MinValueValidator(1)])
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    semester = models.IntegerField(default=0, verbose_name="Semester number", validators=[MaxValueValidator(10),
                                                                              MinValueValidator(1)])
    
    def __str__(self):
        return self.group + " " + self.discipline


class AverageMark(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    quality = models.IntegerField(default=5, validators=[MaxValueValidator(10),
                                                        MinValueValidator(1)])
    methodological_support = models.IntegerField(default=5, validators=[MaxValueValidator(10),
                                                                        MinValueValidator(1)])
    objectivity = models.IntegerField(default=5, validators=[MaxValueValidator(10),
                                                            MinValueValidator(1)])
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    semester = models.IntegerField(default=0, verbose_name="Semester number", validators=[MaxValueValidator(10),
                                                                                            MinValueValidator(1)])
    
    def __str__(self):
        return "Average " + self.group + " " + self.discipline