from django.contrib import admin
# Register your models here.

from .models import Teacher,CourseReview,Student,Category,Course,CourseCurriculum,Blog,BlogReview,Contact


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(CourseReview)
class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(CourseCurriculum)
class CourseCurriculumAdmin(admin.ModelAdmin):
    list_display = ['id']
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id']
    
@admin.register(BlogReview)
class BlogReviewAdmin(admin.ModelAdmin):
    list_display = ['id']
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id']
    


#admin.site.register(Student, StudentAdmin)
#admin.site.register(Teacher, TeacherAdmin)
#admin.site.register(Review, ReviewAdmin)
#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Course, CourseAdmin)
#admin.site.register(CourseCurriculum, CourseCurriculumAdmin)



