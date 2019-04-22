from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def hello_response(request):
    return HttpResponse("Hello Django responses!    Lesson 2")

def http_redirect(request):
    return redirect('/lesson-two-responses/fun/')

def http_name_redirect(request):
    return redirect("lesson_two_responses:fun")

def fun(request):
    return HttpResponse("Hello redirect !")

def render_html(request):
    _html = """
    <html>
        <head><title>TITLE</title>
        <body>
            <h1 style="color:red">HELLO HTML!</h1>
        </body>
    </html>
"""
    return HttpResponse(_html)

def render_template(request):
    return render(request , "lesson_two_responses/index.html" , {})

def form_handler(request):
    if request.POST:
        return HttpResponse("Request is POST")
    else:
        return HttpResponse("Request is GET!")