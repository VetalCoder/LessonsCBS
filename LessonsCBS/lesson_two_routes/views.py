from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to lesson two!")

def special_case(request):
    return HttpResponse("Welcome to special_case by url: localhost/item/2003")

def year_archive_without_params(request):
    return HttpResponse('Welcome to year_archive_without_params by url: localhost/item-without-params/[0-9]{4,5}. No parameters')

def year_archive(request, a):
    return HttpResponse(f'Welcome to year_archive by url: localhost/item/[0-9]{4,5}. Parameter a is "{a}"; type(a) - {type(a).__name__}')

def month_archive(request, year, month):    
    return HttpResponse(f"Welcome to month_archive by the url: localhost/item([0-9]{4})/([0-9]{2})/   Params: {year}, {month}")

def day_archive(request, year, month, day):
    return HttpResponse('Welcome to day_archive!   Year: {}, Month:{}, Day:{}'.format(year, month, day))

def page(request, num="1"):
    if num == "1":
        return HttpResponse("Вы перешли на первую страницу книги!!!")
    else:
        return HttpResponse(f"Вы перешли на страницy под номером {num}")