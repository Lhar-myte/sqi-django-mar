# Generated by Django 5.1.7 on 2025-03-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='no_of_student',
        ),
        migrations.AddField(
            model_name='department',
            name='dpt_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='no_of_student',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
