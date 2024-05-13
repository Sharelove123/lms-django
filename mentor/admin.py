from django.contrib import admin
# Register your models here.

from .models import Teacher,Review,Student,Category,Course,CourseCurriculum


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
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

#admin.site.register(Student, StudentAdmin)
#admin.site.register(Teacher, TeacherAdmin)
#admin.site.register(Review, ReviewAdmin)
#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Course, CourseAdmin)
#admin.site.register(CourseCurriculum, CourseCurriculumAdmin)



