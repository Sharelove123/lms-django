# Generated by Django 4.2.13 on 2024-05-13 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0014_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images'),
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='course_image'),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='student_images'),
        ),
    ]