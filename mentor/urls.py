from django.contrib import admin
from django.urls import path,include
from mentor import views

app_name = 'mentor'

urlpatterns = [
    path('teachers', views.teachers, name="teachers"),
    path('teachers-single/<int:id>', views.teachers_single, name="teachers-single"),
    path('courses', views.courses, name="courses"),
    path('courses-single/<int:id>', views.courses_single, name="courses-single"),
    path('blog', views.blogs, name="blogs"),
    path('blogs-single/<int:id>', views.blogs_single, name="blogs-single"),
]