# Generated by Django 5.1.3 on 2024-11-19 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0006_course_owner_lesson_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course",
            options={
                "ordering": ("id",),
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.AlterModelOptions(
            name="lesson",
            options={
                "ordering": ("id",),
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
    ]