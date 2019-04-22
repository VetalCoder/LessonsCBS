"""
Definition of urls for lesson_two_routes.
"""

from django.urls import path, re_path
from . import views

urlpatterns = [
    path("welcome/", views.welcome),              # http://localhost:8000/lesson-two/welcome/
    path("item/2003/", views.special_case),       # http://localhost:8000/lesson-two/item/2003/
    re_path(r"^item-without-params/[0-9]{4,5}$", views.year_archive_without_params),       # http://localhost:8000/lesson-two/item-without-params/4565
    re_path(r"^item/([0-9]{4,5})$", views.year_archive),                                   # http://localhost:8000/lesson-two/item/1240

    # docs: https://docs.djangoproject.com/en/2.2/topics/http/urls/#path-converters
    #path("item/<int:a>", views.year_archive),                                               # http://localhost:8000/lesson-two/item/1240

    re_path(r'^item/([0-9]{4})/([0-9]{2})$', views.month_archive, name="month_archive"),        # http://localhost:8000/lesson-two/item/2017/10
    re_path(r'^item/(?P<year>[\d]{4})/(?P<month>[0-9]{2})/(?P<day>[\d]{2})/$', views.day_archive , name="day_archive"), # http://localhost:8000/lesson-two/item/2000/01/05/

    # book
    path('book/', views.page, name="page"),                                     # http://localhost:8000/lesson-two/book
    re_path(r'book/page(?P<num>[0-9]+)/$', views.page, name="page"),            # http://localhost:8000/lesson-two/book/page99/

]
