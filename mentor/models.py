from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name='student')
    image = models.ImageField(upload_to='student_images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    
    
class Teacher(models.Model):
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='teacher')
    image = models.ImageField(upload_to='teacher_images', null=True, blank=True)
    position = models.CharField(max_length=20)
    about = models.TextField(max_length=2000,null=False,blank=False)
    achievements = models.TextField(max_length=1500,null=False,blank=False)
    objectives = models.TextField(max_length=1500,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    
    
    def __str__(self):
        return self.teacher.username



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses_taught')
    students = models.ManyToManyField(Student, related_name='courses_enrolled', blank=True)
    favorite = models.ManyToManyField(Student, related_name='courses_favorite', blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='category')
    duration_hours = models.IntegerField(default=10)
    lectures = models.IntegerField(default=9)
    quizzes = models.IntegerField(default=5)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    course_summary = models.TextField()
    requirements = models.TextField()
    image = models.ImageField(upload_to='course_image', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name


class CourseCurriculum(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='curriculum_course')
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()

    def __str__(self):
        return self.title
    
class CourseReview(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE, related_name='review_student')
    comment = models.TextField(max_length=800,null=False,blank=False)
    rateing = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='review_course',null=True)
    
    
    
    

class Blog(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='blog_teacher')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='blog_category')
    content = models.TextField(null=False,blank=False)
    image = models.ImageField(upload_to='blog_images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    
class BlogReview(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE, related_name='blog_review_student')
    comment = models.TextField(max_length=800,null=False,blank=False)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='review_blog_content',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)



class Contact(models.Model):
    yourname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.yourname} - {self.subject}"

    
    
    
    
    
    

     
    
    