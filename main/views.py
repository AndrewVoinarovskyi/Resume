from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def resume(request):
    return render(request, 'main/resume.html')