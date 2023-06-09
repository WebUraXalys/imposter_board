# Generated by Django 4.2 on 2023-04-12 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_alter_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='Примітка'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.faculty'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Discipline name'),
        ),
    ]
