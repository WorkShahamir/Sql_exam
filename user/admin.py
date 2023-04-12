from django.contrib import admin
from .models import Student, Mentor, Course, Language

admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Course)
admin.site.register(Language)
