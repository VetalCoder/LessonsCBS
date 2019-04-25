from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse

import datetime

# Create your views here.

# With module loader
#def view(request):
#    list  = [0, 232, 45, 123, 4, 53423, 54, 23]
#    template  = loader.get_template('lesson_third_templates/index.html')
#    context = {
#        "test": "TEXT FOR TEST!",
#        "list": list,
#        "name": "Guido",
#        "surname": "van Rossum",
#        "coords": {
#            "x": "x coords",
#            "y": "y coords",
#        },
#        #'list': [1, 2, 3, 4]
#    }
#    return HttpResponse(template.render(context, request))


# With function render
def view(request):
    list = [0, 232, 45, 123, 0, 4, 53423, 54, 23]
    context = {
        "test": "TEXT FOR TEST!",
        "list": list,
        "name": "Guido",
        "surname": "van Rossum",
        "coords": {
            "x": "x coords",
            "y": "y coords",
        },
        #'list': [1, 2, 3, 4]
    }
    return render(request, 'lesson_third_templates/index.html', context)


# docs: https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#built-in-filter-reference
def filter(request):
    array_for_sort  = [
        {'name': 'zed', 'age': 19},
        {'name': 'amy', 'age': 22},
        {'name': 'joe', 'age': 31},
    ]

    context = {
        "name_low": "LOWER",
        "value" : 9,
        "first" : [1, 2, 3, 4],
        "second" : [5, 6, 7, 8],
        "str": "I'm using Django",
        "date": datetime.datetime.now(),
        "empty_one": "",
        "for_sort": array_for_sort,
        "float": 32.22364,
        "number": 12345678,
        "boolean_var": None,
        'name': "alex"
    }
    return render(request, "lesson_third_templates/filters.html", context)


# docs: https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#built-in-tag-reference
def tags_if(request):
    list = [1, 2, 3, 4, 5, 6]
    var1 = "var1"
    var2 = "var2"
    var3 = "var3"
    obj = {
        'name' : "Guido",
        'surname' : "van Rossum"
    }

    context = {
        "x" : "x value",
        'user_' : "Admin",
        'list' : list,
        'value' : 10,
        'obj' : obj,        
        "greetings": ["hello", "abc", "xsa"],
        "a": 100,
        "b": 10,
        "c": 1,
        #'var1' : "var1",
        'var2' : "var2",
        #'var3' : "var3",
    }
    return render(request, 'lesson_third_templates/tags_if.html', context)

def tags_for(request):
    list = [1, 2, 3, 4, 5, 6]
    empty = []
    context = {
        "list": list,
        'empty' : empty,
    }
    return render(request, 'lesson_third_templates/tags_for.html', context)

def tag_regroup(request):
    people = [
        {'first_name': 'George', 'last_name': 'Bush', 'gender': 'Male'},
        {'first_name': 'Bill', 'last_name': 'Clinton', 'gender': 'Male'},
        {'first_name': 'Margaret', 'last_name': 'Thatcher', 'gender': 'Female'},
        {'first_name': 'Condoleezza', 'last_name': 'Rice', 'gender': 'Female'},
        {'first_name': 'Pat', 'last_name': 'Smith', 'gender': 'Unknown'},
    ]
    people_for_test = [
        {'first_name': 'Bill', 'last_name': 'Clinton', 'gender': 'Male'},
        {'first_name': 'Pat', 'last_name': 'Smith', 'gender': 'Unknown'},
        {'first_name': 'Margaret', 'last_name': 'Thatcher', 'gender': 'Female'},
        {'first_name': 'George', 'last_name': 'Bush', 'gender': 'Male'},
        {'first_name': 'Condoleezza', 'last_name': 'Rice', 'gender': 'Female'},
    ]
    context = {
        "people": people,
        "people_for_test": people_for_test,
    }
    return render(request, 'lesson_third_templates/tags_regroup.html', context)


# Inheritance templates
def base(request):
    context = {}
    return render(request, 'lesson_third_templates/inheritanse/base.html', context)

def adrian(request):
    context= {
        'name' : 'Адриан',
        'surname' : 'Головатый',
    }
    return render(request, "lesson_third_templates/inheritanse/adrian.html", context)

def releases(request):
    obj = (
        {"year": 2015 , "version" : "1.8"},
        {"year": 2016 , "version" : "1.9"},
        {"year": "2016-2017", "version" : "1.10"},
        {"year": 2017 , "version" : "1.11"},
        {"year": 2018 , "version" : "2.0"},
        {"year": 2018 , "version" : "2.1"},
        {"year": 2019 , "version" : "2.2"},
    )
    context = {
        'obj': obj,
    }
    return render(request, "lesson_third_templates/inheritanse/releases.html", context)