# Generated by Django 4.2.13 on 2024-05-20 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0020_contact_delete_blogreviewreply'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='CourseReview',
        ),
    ]
