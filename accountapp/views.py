from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# 기존 Django 방식
def hello_world(request):
    return HttpResponse('Hello world!')

# DRF 방식
@api_view()
def hello_world_drf(request):
    return Response({"message": "Hello world!"})
