from django.contrib import admin
from student.models import Student

# Register your models here.
# admin 사이트에서 model 객체를 볼 수 있음
admin.site.register(Student)