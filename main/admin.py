from django.contrib import admin
from .models import Student, Class, School, Schedule, Lessons, Teacher, Position
# Register your models here.
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(School)
admin.site.register(Schedule)
admin.site.register(Lessons)
admin.site.register(Teacher)
admin.site.register(Position)