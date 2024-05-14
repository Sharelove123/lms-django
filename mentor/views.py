from django.shortcuts import render
from django.core.paginator import Paginator
from . import models
from django.db.models import Avg
# Create your views here.

def teachers(request):
    queryset = models.Teacher.objects.all()
    paginator = Paginator(queryset, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'mentor/teachers.html',{'page_obj':page_obj})


def teachers_single(request,id):
    teacher = models.Teacher.objects.get(id=id)
    context={'teacher':teacher}
    return render(request,'mentor/teachers-single.html',context=context)


def courses(request):
    queryset = models.Course.objects.all()
    paginator = Paginator(queryset, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'mentor/courses.html',{'page_obj':page_obj})


def courses_single(request,id):
    course = models.Course.objects.get(id=id)
    course_review = models.Review.objects.filter(course=course)
    total_review = course_review.count()
    avg_rateing = course_review.aggregate(rateing=Avg('rateing'))['rateing']
    course_curriculum = models.CourseCurriculum.objects.filter(course=course)

    context={
        'course':course,
        'course_review':course_review,
        'total_review':total_review,
        'avg_rateing':avg_rateing,
        'course_curriculum':course_curriculum
    }
    return render(request,'mentor/courses-single.html',context=context)

def blogs(request):
    queryset = models.Blog.objects.all()
    paginator = Paginator(queryset, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'mentor/blog.html',{'page_obj':page_obj})

import json
def blogs_single(request,id):
    blog = models.Blog.objects.get(id=id)
    blog_review = models.BlogReview.objects.filter(blog=blog)
    userId = request.user
    student = models.Student.objects.get(student=userId)
    studentId = student.id
    studentImage = json.dumps(student.image.url)
    username = json.dumps(student.student.username)

    context={
        'blog':blog,
        'blog_review':blog_review,
        'studentId':studentId,
        'studentImage':studentImage,
        'username':username
    }
    return render(request,'mentor/blog-single.html',context=context)