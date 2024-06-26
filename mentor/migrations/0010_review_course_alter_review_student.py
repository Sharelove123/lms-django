# Generated by Django 4.2.13 on 2024-05-11 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0009_coursecurriculum'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_course', to='mentor.course'),
        ),
        migrations.AlterField(
            model_name='review',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_student', to='mentor.student'),
        ),
    ]
