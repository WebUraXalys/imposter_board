from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Group(models.Model):
    name = models.CharField(max_length=6, verbose_name="Group name")
    disciplines = models.ManyToManyField(Discipline)


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=20, verbose_name="Teacher name")


class Discipline(models.Model):
    name = models.CharField(max_length=20, verbose_name="Discipline name")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Mark(models.Model):
    group = models.ForeignKey(Group)
    quality = models.IntegerField(default=5, validators=[MaxValueValidator(10),
                                                        MinValueValidator(1)])
    methodological_support = models.IntegerField(default=5, validators=[MaxValueValidator(10),
                                                                       MinValueValidator(1)])
    objectivity = models.IntegerField(default=5, validators=[MaxValueValidator(10),
                                                            MinValueValidator(1)])
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    semester = models.IntegerField(verbose_name="Semester number", validators=[MaxValueValidator(10),
                                                                              MinValueValidator(1)])


class AverageMark(models.Model):
    group = models.ForeignKey(Group)
    quality = models.IntegerField(default=5, validators=[MaxValueValidator(10),
                                                        MinValueValidator(1)])
    methodological_support = models.IntegerField(default=5, validators=[MaxValueValidator(10),
                                                                       MinValueValidator(1)])
    objectivity = models.IntegerField(default=5, validators=[MaxValueValidator(10),
                                                            MinValueValidator(1)])
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    semester = models.IntegerField(verbose_name="Semester number", validators=[MaxValueValidator(10),
                                                                              MinValueValidator(1)])