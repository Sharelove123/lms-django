from django.shortcuts import render
from django.core.paginator import Paginator
from . import models
from django.db.models import Avg
from django.http import JsonResponse
from django.http import HttpResponse  
from .forms import ContactForm
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
    course_review = models.CourseReview.objects.filter(course=course)
    total_review = course_review.count()
    avg_rateing = course_review.aggregate(rateing=Avg('rateing'))['rateing']
    course_curriculum = models.CourseCurriculum.objects.filter(course=course)
    
    if request.user.is_authenticated and models.Student.objects.get(student = request.user) in course.students.all():
        userId = request.user
        student = models.Student.objects.get(student=userId)
        studentId = student.id
        studentImage = json.dumps(student.image.url)
        username = json.dumps(student.student.username)

        context={
            'courseId':course.id,
            'course_review':course_review,
            'total_review':total_review,
            'avg_rateing':avg_rateing,
            'course_curriculum':course_curriculum,
            'studentId':studentId,
            'studentImage':studentImage,
            'username':username,
            'enrolled':True,
        }
    else:
        context={
                'course':course,
                'course_review':course_review,
                'total_review':total_review,
                'avg_rateing':avg_rateing,
                'course_curriculum':course_curriculum,
                'enrolled':False
            }
    return render(request,'mentor/courses-single.html',context=context)

def blogs(request):
    queryset = models.Blog.objects.all()
    paginator = Paginator(queryset, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'mentor/blog.html',{'page_obj':page_obj})

import json
from django.db.models import OuterRef,Subquery

def blogs_single(request,id):
    
    blog = models.Blog.objects.get(id=id)
    blog_review = models.BlogReview.objects.filter(blog=blog)
    
    if request.user.is_authenticated:
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
        
    else:
        context = {
            'blog':blog,
            'blog_review':blog_review,
        }
    return render(request,'mentor/blog-single.html',context=context)


def about(request):
    students_count = models.Student.objects.all().count()
    teachers_count = models.Teacher.objects.all().count()
    courses_count = models.Course.objects.all().count()
    context = {
        'studentsCount': students_count,
        'teachersCount': teachers_count,
        'coursesCount' : courses_count,
    }
    return render(request,'mentor/about.html',context=context)

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('HX-Request'):
                return HttpResponse('Thanks for contacting us! ✅')
            else:
                return HttpResponse('Your form submission was unsuccessful ❌')
        else:
            return HttpResponse(f'Your form submission was unsuccessful ❌. Please would you correct the errors? The current errors: {form.errors}')
    else:
        form = ContactForm()

    return render(request, 'mentor/contact.html', {'form': form})
