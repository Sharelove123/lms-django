# Generated by Django 4.2.13 on 2024-05-10 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0004_alter_teacher_about_alter_teacher_achievements_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='about',
            field=models.TextField(max_length=2000),
        ),
    ]