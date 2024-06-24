from django.urls import path
from accountapp.views import hello_world, hello_world_drf
from student.api import StudentList, StudentDetail

app_name = "student"

urlpatterns = [
    path('list/', StudentList.as_view(), name='list'),
    path('list/<int:student_id>', StudentDetail.as_view(), name='detail'),
]