# Generated by Django 4.2.13 on 2024-05-22 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0022_rename_rateing_coursereview_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursereview',
            old_name='rating',
            new_name='rateing',
        ),
    ]
