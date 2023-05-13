from django.shortcuts import render
from django.http import HttpResponse

def courses(request, course):
    list_courses = {
        'anatomy':'This is the study of human parts',
        'philosophy': 'the study of nature and everything related to it',
        'physiology':'The study of the functions of the parts of the body',
    }
    
    description = list_courses[course]
    return HttpResponse(f"<p>{course}<p/>" + description)

def index(request):
    return render(request, 'index.html', {})