# Generated by Django 4.2.13 on 2024-05-15 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0017_blogreviewreply_replyed_to_alter_blogreview_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogreviewreply',
            name='replyed_to',
        ),
    ]