from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from . import models
from django.db.models import Case, When, CharField, Value, F, Avg, ImageField
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
    
    if models.CourseReview.objects.filter(course=course).exists():
        course_review = models.CourseReview.objects.filter(course=course)
        total_review = course_review.count()
        avg_rateing = course_review.aggregate(rateing=Avg('rateing'))['rateing']
    else:
        course_review = []
        avg_rateing = 0
        total_review = 0
    course_curriculum = models.CourseCurriculum.objects.filter(course=course)
    context = {}
    if models.Student.objects.filter(student=request.user).exists():
        if request.user.is_authenticated and models.Student.objects.get(student = request.user) in course.students.all():
            userId = request.user
            student = models.Student.objects.get(student=userId)
            studentId = student.id
            studentImage = json.dumps(student.image.url)
            username = json.dumps(student.student.username)

            context={
                'course':course,
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
    category = models.Category.objects.all()[:10]
    
    if request.user.is_authenticated and models.Student.objects.filter(student=request.user).exists():
        userId = request.user
        student = models.Student.objects.get(student=userId)
        
        studentId = student.id
        studentImage = json.dumps(student.image.url)
        username = json.dumps(student.student.username)
        

        context={
            'blog':blog,
            'blog_review':blog_review,
            'student': True,
            'studentId':studentId,
            'studentImage':studentImage,
            'username':username,
            'category':category
        }
        
    else:
        context = {
            'blog':blog,
            'blog_review':blog_review,
            'student': False,
            'category':category
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



def shops(request):
    queryset = models.Product.objects.all()
    paginator = Paginator(queryset, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'mentor/shop.html',{'page_obj':page_obj})


def shops_single(request,id):
    product = models.Product.objects.get(id=id)
    product_review = models.ReviewProduct.objects.filter(product=product)          
    total_review = product_review.count()
    avg_rateing = product_review.aggregate(rateing=Avg('rateing'))['rateing']
    
    
    if request.user.is_authenticated:
        user = request.user
        userId = json.dumps(user.id)
        if models.Student.objects.filter(student=user).exists():
            student = models.Student.objects.get(student=user)
            userImage = json.dumps(student.image.url)
            
        if models.Teacher.objects.filter(teacher=user).exists():
            teacher = models.Teacher.objects.get(teacher=user)
            userImage = json.dumps(teacher.image.url)
        username = json.dumps(user.username)

        context={
            'productId':json.dumps(product.id),
            'product':product,
            'product_review':product_review,
            'total_review':total_review,
            'avg_rateing':avg_rateing,
            'userId':userId,
            'userImage':userImage,
            'username':username,
        }
    else:
        context={
                'product':product,
                'productId':product.id,
                'product_review':product_review,
                'total_review':total_review,
                'avg_rateing':avg_rateing,
                'enrolled':False
            }

    return render(request,'mentor/shop-single.html',context=context)



def dashboard(request):
    user = request.user
    category = models.Category.objects.all()
    
    if models.Student.objects.filter(student=user).exists() and models.Teacher.objects.filter(teacher=user).exists():
        student = models.Student.objects.get(student=user)
        teacher = models.Teacher.objects.get(teacher=user)
        enrolled_courses = student.courses_enrolled.all()
        your_courses = teacher.courses_taught.all()
        your_blogs = teacher.blog_teacher.all()
        context = {
            'student':student,
            'teacher':teacher,
            'enrolled_courses': enrolled_courses,
            'your_courses':your_courses,
            'your_blogs':your_blogs,
            'category':category,
            
        }
        
        
    elif models.Student.objects.filter(student=user).exists():
        student = models.Student.objects.get(student=user)
        teacher = None
        enrolled_courses = student.courses_enrolled.all()
        print(enrolled_courses)
        context = {
            'student':student,
            'teacher':None,
            'enrolled_courses': enrolled_courses,
        }
        
        
    elif models.Teacher.objects.filter(teacher=user).exists():
        student = None
        teacher = models.Teacher.objects.get(teacher=user)
        your_courses = teacher.courses_taught.all()
        your_blogs = teacher.blog_teacher.all()
        
        context = {
            'student':None,
            'teacher':teacher,
            'your_courses':your_courses,
            'your_blogs':your_blogs,
            'category':category,
        }

        
        
    return render(request,'mentor/dashboard.html',context=context)


import datetime
def course_create_view(request):
    if request.user.is_authenticated and models.Teacher.objects.filter(teacher = request.user).exists():
        if request.method == 'POST':
            category = models.Category.objects.get(name= request.POST['category'])
            duration =  request.POST['duration']
            duration = datetime.datetime.strptime(duration, '%H:%M')
            hours = duration.hour
            minutes = duration.minute   
            total_course_duration = datetime.timedelta(hours=hours, minutes=minutes)
            course = models.Course.objects.create(
                teacher=models.Teacher.objects.get(teacher=request.user),
                name = request.POST['name'],
                category = category,
                duration_hours= total_course_duration,
                lectures= request.POST['noOfLeacture'],
                quizzes=request.POST['quizzes'],
                price=request.POST['price'],
                course_summary=request.POST['course_summary'],
                requirements=request.POST['requirements'],
                image = request.FILES['courseImage']
            )
            
            for leacture in range(int(request.POST['noOfLeacture'])):
                lectureNo = leacture+1
                title = f'lectureTitle{lectureNo}'
                description = f'lectureDescription{lectureNo}'
                duration =  f'lectureDuration{lectureNo}'
                duration = request.POST[duration]
                duration = datetime.datetime.strptime(duration, '%H:%M')
                video = f'lectureVideo{lectureNo}'
                
                
                hours = duration.hour
                minutes = duration.minute
                
                total_leacture_duration = datetime.timedelta(hours=hours, minutes=minutes)
                
                models.CourseCurriculum.objects.create(
                    course = course,
                    title = request.POST[title],
                    description = request.POST[description],
                    duration = total_leacture_duration,
                    video = request.FILES[video],          
                )
                
            return HttpResponse('Your Course Created successful')
        
        

def blog_create_view(request):
    if request.user.is_authenticated and models.Teacher.objects.filter(teacher = request.user).exists():
        if request.method == 'POST':
            category = models.Category.objects.get(name = request.POST['blogCategory'])
            teacher = models.Teacher.objects.get(teacher = request.user)
            models.Blog.objects.create(
                teacher = teacher,
                title = request.POST['blogTitle'],
                category = category,
                content = request.POST['blogContent'],
                image = request.FILES['blogImage']
            )
            return HttpResponse('Your Blog Created successful')


def delete_user(request):
    user = request.user
    user.delete()
    print('user deleted')
    return redirect('core:home')

def getdashboard(request):
    if request.user.is_authenticated:
        return redirect('mentor:dashboard')
    