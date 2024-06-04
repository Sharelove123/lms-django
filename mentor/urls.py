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
    path('shop', views.shops, name="shops"),
    path('shop-single/<int:id>', views.shops_single, name="shop-single"),
    path('about', views.about, name="about"),
    path('contact', views.contact_us, name="contact"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('course/create/', views.course_create_view, name='course_create'),
    path('blog/create/', views.blog_create_view, name='blog_create'),
]
